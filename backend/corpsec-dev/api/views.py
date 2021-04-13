from django.shortcuts import render
from rest_framework.response import Response
from mptt.templatetags.mptt_tags import cache_tree_children
from rest_framework import viewsets
from depts.models import Department
from depts.serializers import DeptSerializer
from rest_framework import generics
import json
from django.http import HttpResponse

"""
class CompanyListView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    #queryset = cache_tree_children(queryset)
    serializer_class = DeptSerializer
"""
def intial_state(request):
    #queryset = Department.objects.all()
    #node = Department.objects.get(level=0, id=1)
    
    #print ("node", node.id)
    #queryset = cache_tree_children(queryset)
    #serializer_class = DeptSerializer
    #result = recursive_node_to_dict(node)
    #print("result", result)
    root_nodes = cache_tree_children(Department.objects.all())
    print("root node", root_nodes)
    dicts = []
    for n in root_nodes:
        dicts.append(recursive_node_to_dict(n))

    print("result", json.dumps(dicts, indent=4))

    list_result = json.dumps(dicts, indent=4)
    #return JsonResponse(list_result, safe=False)
    return HttpResponse(list_result)

def recursive_node_to_dict(node):
    result = {
        'id': node.id,
        'name': node.name,
    }
    children = [recursive_node_to_dict(c) for c in node.get_children()]
    if children:
        result['children'] = children
    return result


