from rest_framework import status
from rest_framework.response import Response
from urllib.request import urlopen
from django.core.cache import cache
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json

def Stories(values):
    """ Function that take two arguments pass it in list format [i, n]
        return a list with n elements from the hacker-news list starting in the index i
    """
    i= values[0]
    n= values[1]

    urlResponse = json.loads(urlopen("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty").read())
    if n > len(urlResponse):
        return "The n number of stories wanted exceeds the number of stories avalible."
    elif i > len(urlResponse):
        return "The i index required is out of range."
    elif n < 0 or i < 0:
        return "please do not submit negative numbers."

    resentStories = [items for items in urlResponse[i:i+n]]
    return resentStories
    

def wantedStories(resentStories):
    """ Function that take the list returned from the Stories function as argument
        return a list of dictionarys with the id and the title of every story in the list
    """
    wantedStories = [json.loads(urlopen("https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty".format(item)).read()) for item in resentStories]
    detailedStories = [{k:detail[k] for k in ('id', 'title')} for detail in wantedStories]
    return detailedStories


@api_view(['GET'])
def storiesResponse(request):
    """ Function that take the request and validate in wich format its gonna be pass it
        if the information is cached return the same information
        if the information is pass in the url body assing a list with values finded
        if the information is pass in json format assing a list with values finded
        then set the cache information for the next queries
        return a list of dictionarys with the id and the title of every story in the list
    """
    if cache.get('stories') and cache.get('topStories'):
        return JsonResponse(cache.get('stories'), safe=False)
    else:
        json = request.data
        if not json:
            if not request.GET.get('i'):
                return Response('Missing the i value.', status=status.HTTP_400_BAD_REQUEST)
            elif not request.GET.get('n'):
                return Response('Missing the n value.', status=status.HTTP_400_BAD_REQUEST)
            else:
                values =[int(request.GET.get('i')), int(request.GET.get('n'))]
        else:
            values =[int(json['i']), int(json['n'])]
        
        topStories = Stories(values)

        if type(topStories) == str:
            return Response(topStories, status=status.HTTP_400_BAD_REQUEST)
        cache.set('topStories', topStories, 10)

        stories = wantedStories(topStories)
        cache.set('stories', stories, 10)

        return JsonResponse(stories, safe=False)
