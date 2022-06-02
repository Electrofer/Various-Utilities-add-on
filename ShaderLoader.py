import bpy

bl_info = {
    "name": "Shady Stuff (ShaderLoader)",
    "author": "Zircon05",
    "version": (0, 4, 3),
    "blender": (2, 80, 0),
    "location": "Scene Properties > Shady Stuff",
    "description": "Applies a Toon Shader to the selected object (For testing and merging with Various Utilities v0.2)",
    "warning": "In development, bugs may occur",
    "doc_url": "",
    "category": "Utilities",
}



def main(context):
    MatName = "BasicToonShader"
    # Test if material exists
    # If it does not exist, create it:
    Mat = (bpy.data.materials.get(MatName) or 
           bpy.data.materials.new(MatName))

    # Enable 'Use nodes':
    Mat.use_nodes = True
    nodes = Mat.node_tree.nodes
    Object = bpy.context.active_object

    for node in nodes:
        nodes.remove(node)

    # Add a diffuse shader and set its location:    
    DiffuseBSDF = nodes.new('ShaderNodeBsdfDiffuse')
    DiffuseBSDF.location = (100,100)
    
    ShaderToRGB = nodes.new('ShaderNodeShaderToRGB')
    ShaderToRGB.location = (325,100)
    
    ColorRamp = nodes.new('ShaderNodeValToRGB')
    ColorRamp.location = (550, 100)
    
    MaterialOutput = nodes.new('ShaderNodeOutputMaterial')
    MaterialOutput.location = (875, 100)
    
    Mat.node_tree.links.new(ShaderToRGB.inputs[0], DiffuseBSDF.outputs[0])
    Mat.node_tree.links.new(ColorRamp.inputs[0], ShaderToRGB.outputs[0])
    Mat.node_tree.links.new(MaterialOutput.inputs[0], ColorRamp.outputs[0])
    
    bpy.data.materials["BasicToonShader"].node_tree.nodes["ColorRamp"].label = "ColorRamp/Use it to modify the Shader"
    
    Object.active_material = Mat


class BasicToonShaderAdder(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.btsa"
    bl_label = "Add Basic Toon Shader"

    def execute(self, context):
        main(context)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(BasicToonShaderAdder.bl_idname, text=BasicToonShaderAdder.bl_label)




class LayoutPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Shady Stuff"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Big render button
        layout.label(text="Shaders:")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.btsa")


def register():
    bpy.utils.register_class(LayoutPanel)
    bpy.utils.register_class(BasicToonShaderAdder)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


def unregister():
    bpy.utils.unregister_class(LayoutPanel)
    bpy.utils.unregister_class(BasicToonShaderAdder)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()
