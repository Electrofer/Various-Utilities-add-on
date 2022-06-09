bl_info = {
    "name": "Various Utilities",
    "author": "Electrofer",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "In the Scene Properties menu",
    "description": "Makes your life a little easier. The mayority of buttons don't work. Using this depricated version is strongly disadvised",
    "warning": "In development, bugs may occur. Delete Default Cube and Destroy Default Cube buttons don't work. Delete Default Cube just deletes the selected mesh, careful with that.",
    "doc_url": "",
    "category": "Utilites",
}


import bpy
import time






def main(context):

    bpy.ops.mesh.primitive_plane_add(size=15, enter_editmode=False, align='WORLD', location=(0, 7.5, 7.5), rotation=(1.57, 0, 0), scale=(1, 1, 1))
    bpy.ops.mesh.primitive_plane_add(size=15, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    bpy.ops.mesh.primitive_plane_add(size=15, enter_editmode=False, align='WORLD', location=(-7.5, 0, 7.5), rotation=(0, 1.57, 0), scale=(1, 1, 1))

def DDC(context):

    bpy.ops.object.delete(use_global=False, confirm=False)







class SceneCreator(bpy.types.Operator):
    """Creates a three plane basic scene"""
    bl_idname = "object.scene_creator"
    bl_label = "Basic Scene Creator"

    def execute(self, context):
        main(context)
        return {'FINISHED'}

class DefaultCubeDeleter(bpy.types.Operator):
    """Deletes the thing you have selected (for now), dosen't have to be a default cube"""
    bl_idname = "object.delete_dflt_cube"
    bl_label = "Delete Default Cube"

    def execute(self, context):
        DDC(context)
        return {'FINISHED'}

class DefaultCubeDestroyer(bpy.types.Operator):
    """Destroys default cubes (and other things lol)"""
    bl_idname = "object.destroy_dflt_cube"
    bl_label = "Destroy Default Cube"

    def execute(self, context):
        DCD(context)
        return {'FINISHED'}




def menu_func(self, context):
    self.layout.operator(SimpleOperator.bl_idname, text=SimpleOperator.bl_label)




class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Various Utilities"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Scene button
        layout.label(text="Buttons:")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.scene_creator")

        # Delete Default Cube Button
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.delete_dflt_cube")

        # Destroy Default Cube Button
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.destroy_dflt_cube")


def register():
    bpy.utils.register_class(DefaultCubeDestroyer)
    bpy.utils.register_class(DefaultCubeDeleter)
    bpy.utils.register_class(SceneCreator)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    bpy.utils.register_class(LayoutDemoPanel)


def unregister():
    bpy.utils.unregister_class(DefaultCubeDestroyer)
    bpy.utils.unregister_class(DefaultCubeDeleter)
    bpy.utils.unregister_class(LayoutDemoPanel)
    bpy.utils.unregister_class(SceneCreator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()
