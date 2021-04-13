
First part
It includs video.
Random subsidiries using django-mptt in django.
It requires to get tree structure based on depth-first search algorithm and django-mptt.
actually I used cache_tree_children for dfs.
1)This is backend part:

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

It takes tree structure specialized in parent-children relation.

2) API
Communication and data stream using api.

export const api = {
    post: async (path, body) => {
      const response = await fetch(`/api/${path}`, options('POST', body))
      return await response.json()
    },
    get: async (path) => {
      const response = await fetch(`http://localhost:8000/api/${path}`, options('GET'))
      return await response.json()
    },
    patch: async (path, body) => {
      const response = await fetch(`/api/${path}`, options('PATCH', body))
      return await response.json()
    },
    delete: async (path) => {
      const response = await fetch(`/api/${path}`, options('DELETE'))
      return await response.json()
    },
}

3)Front-end

return (
          
          <>
            <Div>
                <Div style={styles.searchBox}>
                    <Div className="input-group">
                        <span className="input-group-addon">
                            <i className="fa fa-search"/>
                        </span>
                    </Div>
                </Div>
                <Div style={styles.component}>
                    <Treebeard
                        data={props.data}
                        onToggle={onToggle}
                        onSelect={onSelect}
                        decorators={{...decorators, Header}}
                        customStyles={{
                            header: {
                                title: {
                                    color: 'red'
                                }
                            }
                        }}
                    />
                </Div>
                <Div style={styles.component}>
                    <NodeViewer node={state.cursor}/>
                </Div>
            </Div>
          </>                        
 );

By using SSR, It enables followings
 - Server sends Ready to be rendered HTML response to your Browser (Page is Loading)
 - Browser Renders HTML of the page and downloads JS (Page Loaded)
 - Browser executes React
 - Page is now Interactable

*********************************************************************************
I have focused on only implementation of logic.
There was not plenty of feedback for UI implementation.
If you have feedback for UI or anything else, Please inform me.
I have added to git.