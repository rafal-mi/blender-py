import bpy 
import bmesh
import functools 

interval = 1.0
edge_index = 0

def select_edge(bm, i):
    bpy.ops.mesh.select_all(action="DESELECT")
    bm.edges.ensure_lookup_table() 
    bm.edges[i].select = True
         
def every_interval():
    global edge_index
    print("In timer function")    
    select_edge(bm, edge_index)
    edge_index += 1
    if edge_index >= len(bm.edges):
        edge_index = 0
    return interval

def after(fun):
    print("Unregistering")
    bpy.app.timers.unregister(fun)
         
# Must start in object mode 
#bpy.ops.object.mode_set(mode='OBJECT') 
#bpy.ops.object.select_all(action='SELECT') 
#bpy.ops.object.delete() 

# bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0)) 
# bpy.ops.object.mode_set(mode='EDIT')

bm = bmesh.from_edit_mesh(bpy.context.object.data)

bpy.app.timers.register(every_interval)
bpy.app.timers.register(functools.partial(after, every_interval), first_interval=15.0)


