import bpy 
import bmesh 

# Delete all objects 
def delete_all(): 
    if(len(bpy.data.objects) != 0): 
        bpy.ops.object.select_all(action='SELECT') 
        bpy.ops.object.delete(use_global=False)

def loop_cut():
    bpy.ops.mesh.loopcut_slide(
        MESH_OT_loopcut={
            "number_cuts": 3, 
            "smoothness":0, 
            "falloff":
            'INVERSE_SQUARE', 
            "object_index":0, 
            "edge_index":11, 
            "mesh_select_mode_init":(True, False, False)
        }, 
        TRANSFORM_OT_edge_slide={
            "value":0.0, 
            "single_side":False, 
            "use_even":False, 
            "flipped":False, 
            "use_clamp":True, 
            "mirror":True, 
            "snap":False, 
            "snap_elements":{
                'INCREMENT'
            }, 
            "use_snap_project":False, 
            "snap_target":'CLOSEST', 
            "use_snap_self":True, 
            "use_snap_edit":True, 
            "use_snap_nonedit":True, 
            "use_snap_selectable":False, 
            "snap_point":(0, 0, 0), 
            "correct_uv":True, 
            "release_confirm":False, 
            "use_accurate":False
        }
    )


def move_edge():
    bm = bmesh.from_edit_mesh(bpy.context.object.data)

    # Deselect all verts, edges, faces 
    bpy.ops.mesh.select_all(action="DESELECT")

    # Select an edge 
    bm.edges.ensure_lookup_table() 
    bm.edges[2].select = True




# Must start in object mode 
# bpy.ops.object.mode_set(mode='OBJECT') 
# bpy.ops.object.select_all(action='SELECT') 
# bpy.ops.object.delete() 
delete_all()

# Create a cube and enter Edit Mode 
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0)) 
bpy.ops.object.mode_set(mode='EDIT') 

loop_cut()
move_edge()

