import bpy 
import bmesh 

# Must start in object mode 
#bpy.ops.object.mode_set(mode='OBJECT') 
#bpy.ops.object.select_all(action='SELECT') 
#bpy.ops.object.delete() 

# Create a cube and enter Edit Mode 
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0)) 
bpy.ops.object.mode_set(mode='EDIT') 

bm = bmesh.from_edit_mesh(bpy.context.object.data)

# Deselect all verts, edges, faces 
bpy.ops.mesh.select_all(action="DESELECT")

# Select an edge 
bm.edges.ensure_lookup_table() 
bm.edges[2].select = True
