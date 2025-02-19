# Scale oneface

# Chris Conlan
# The Blender Pytho API
# Listing 3-5

import bpy 
import bmesh 

# Must start in object mode 
bpy.ops.object.mode_set(mode='OBJECT') 
bpy.ops.object.select_all(action='SELECT') 
bpy.ops.object.delete() 

# Create a cube and enter Edit Mode 
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0)) 
bpy.ops.object.mode_set(mode='EDIT') 

# Set to "Face Mode" for easier visualization 
bpy.ops.mesh.select_mode(type = "FACE") 

# Register bmesh object and select various parts 
bm = bmesh.from_edit_mesh(bpy.context.object.data) 

# Deselect all verts, edges, faces 
bpy.ops.mesh.select_all(action="DESELECT") 

# Select a face 
bm.faces.ensure_lookup_table() 
bm.faces[5].select = True 

bpy.ops.transform.resize(value=(0.760051, 0.760051, 0.760051))

# Select an edge 
# bm.edges.ensure_lookup_table() 
# bm.edges[7].select = True 

# Select a vertex 
# bm.verts.ensure_lookup_table() 
# bm.verts[5].select = True

