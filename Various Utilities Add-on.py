import bpy


bl_info = {
    "name": "Various Utilities",
    "author": "Electrofer",
    "version": (0, 4, 5, 1),
    "blender": (2, 80, 0),
    "location": "In the Scene Properties menu",
    "description": "Makes your life a little easier.",
    "warning": "In development, bugs may occur",
    "doc_url": "",
    "category": "Utilites",
}


class ErrorMenuNoCubes(bpy.types.Menu):
    bl_label = "An error happened"
    bl_idname = "error_menu_no_cubes"

    def draw(self, context):
        layout = self.layout

        layout.label(text="There are no cubes in the scene.")

class ErrorMenuNoObjectSelected(bpy.types.Menu):
    bl_label = "An error happened"
    bl_idname = "error_menu_no_object_selected"

    def draw(self, context):
        layout = self.layout

        layout.label(text="There are no selected objects to apply the shader.")

class ErrorMenuNoObjectSelectedB(bpy.types.Menu):
    bl_label = "Something could not be resolved"
    bl_idname = "error_menu_no_object_selected_b"

    def draw(self, context):
        layout = self.layout

        layout.label(text="There is no object selected. In order to do the full action, please select an object.")

class MenuObjectAlreadyHasReflections(bpy.types.Menu):
    bl_label = "Something went wrong"
    bl_idname = "menu_object_already_has_reflections"

    def draw(self, context):
        layout = self.layout

        layout.label(text="Object already has reflections")



class CoreFunctions(bpy.types.Operator):


    def SimpleSceneAdder(context):

        bpy.ops.mesh.primitive_plane_add(size=15, enter_editmode=False, align='WORLD', location=(0, 7.5, 7.5), rotation=(1.57, 0, 0), scale=(1, 1, 1))
        bpy.ops.mesh.primitive_plane_add(size=15, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.ops.mesh.primitive_plane_add(size=15, enter_editmode=False, align='WORLD', location=(-7.5, 0, 7.5), rotation=(0, 1.57, 0), scale=(1, 1, 1))


    def DefCubeDel(context):
        # Deselect all
        try:
            bpy.ops.object.select_all(action='DESELECT')

            bpy.data.objects['Cube'].select_set(True)

            with context.temp_override():
                bpy.ops.object.delete()

        except:
            bpy.ops.wm.call_menu(name=ErrorMenuNoCubes.bl_idname)

    def BasicToonShaderAdder(context):

        try:
            MatName = "Basic Toon Shader"
            # Test if material exists
            # If it does not exist, create it:
            Mat = (bpy.data.materials.get(MatName) or
                   bpy.data.materials.new(MatName))

            # Enable 'Use nodes':
            Mat.use_nodes = True
            Nodes = Mat.node_tree.nodes
            Object = bpy.context.active_object

            for node in Nodes:
                Nodes.remove(node)

            # Add a diffuse shader and set its location:
            DiffuseBSDF = Nodes.new('ShaderNodeBsdfDiffuse')
            DiffuseBSDF.location = (100,100)

            ShaderToRGB = Nodes.new('ShaderNodeShaderToRGB')
            ShaderToRGB.location = (325,100)

            ColorRamp = Nodes.new('ShaderNodeValToRGB')
            ColorRamp.location = (550, 100)

            MaterialOutput = Nodes.new('ShaderNodeOutputMaterial')
            MaterialOutput.location = (875, 100)

            Mat.node_tree.links.new(ShaderToRGB.inputs[0], DiffuseBSDF.outputs[0])
            Mat.node_tree.links.new(ColorRamp.inputs[0], ShaderToRGB.outputs[0])
            Mat.node_tree.links.new(MaterialOutput.inputs[0], ColorRamp.outputs[0])

            bpy.data.materials["Basic Toon Shader"].node_tree.nodes["ColorRamp"].label = "ColorRamp/Use it to modify the Shader"

            Object.active_material = Mat

        except:
            bpy.ops.wm.call_menu(name=ErrorMenuNoObjectSelected.bl_idname)

    def CopperShaderAdder(context):

        try:
            MatName = "Copper"
            # Test if material exists
            # If it does not exist, create it:
            Mat = (bpy.data.materials.get(MatName) or
                   bpy.data.materials.new(MatName))

            # Enable 'Use nodes':
            Mat.use_nodes = True
            Nodes = Mat.node_tree.nodes
            Object = bpy.context.active_object

            for node in Nodes:
                Nodes.remove(node)

            # Add a diffuse shader and set its location:
            PrincipledBSDF = Nodes.new('ShaderNodeBsdfPrincipled')
            PrincipledBSDF.location = (100,100)
            PrincipledBSDF.inputs['Base Color'].default_value = (0.701, 0.254, 0.136, 1)
            PrincipledBSDF.inputs['Metallic'].default_value = 1
            PrincipledBSDF.inputs['Roughness'].default_value = 0.275

            MaterialOutput = Nodes.new('ShaderNodeOutputMaterial')
            MaterialOutput.location = (525, 100)

            Mat.node_tree.links.new(MaterialOutput.inputs[0], PrincipledBSDF.outputs[0])

            Object.active_material = Mat

        except:
            bpy.ops.wm.call_menu(name=ErrorMenuNoObjectSelected.bl_idname)

    def RedCopperShaderAdder(context):

        try:
            MatName = "Red Copper"
            # Test if material exists
            # If it does not exist, create it:
            Mat = (bpy.data.materials.get(MatName) or
                   bpy.data.materials.new(MatName))

            # Enable 'Use nodes':
            Mat.use_nodes = True
            Nodes = Mat.node_tree.nodes
            Object = bpy.context.active_object

            for node in Nodes:
                Nodes.remove(node)

            # Add a diffuse shader and set its location:
            PrincipledBSDF = Nodes.new('ShaderNodeBsdfPrincipled')
            PrincipledBSDF.location = (100,100)
            PrincipledBSDF.inputs['Base Color'].default_value = (0.597, 0.153, 0.082, 1)
            PrincipledBSDF.inputs['Metallic'].default_value = 1
            PrincipledBSDF.inputs['Roughness'].default_value = 0.275

            MaterialOutput = Nodes.new('ShaderNodeOutputMaterial')
            MaterialOutput.location = (525, 100)

            Mat.node_tree.links.new(MaterialOutput.inputs[0], PrincipledBSDF.outputs[0])

            Object.active_material = Mat

        except:
            bpy.ops.wm.call_menu(name=ErrorMenuNoObjectSelected.bl_idname)

    def UnpolishedAluminumShaderAdder(context):

        try:
            MatName = "Unpolished Aluminum"
            # Test if material exists
            # If it does not exist, create it:
            Mat = (bpy.data.materials.get(MatName) or
                   bpy.data.materials.new(MatName))

            # Enable 'Use nodes':
            Mat.use_nodes = True
            Nodes = Mat.node_tree.nodes
            Object = bpy.context.active_object

            for node in Nodes:
                Nodes.remove(node)

            # Add a diffuse shader and set its location:
            PrincipledBSDF = Nodes.new('ShaderNodeBsdfPrincipled')
            PrincipledBSDF.location = (100,100)
            PrincipledBSDF.inputs['Base Color'].default_value = (0.246, 0.258, 0.266, 1)
            PrincipledBSDF.inputs['Metallic'].default_value = 1
            PrincipledBSDF.inputs['Roughness'].default_value = 0.500

            MaterialOutput = Nodes.new('ShaderNodeOutputMaterial')
            MaterialOutput.location = (525, 100)

            Mat.node_tree.links.new(MaterialOutput.inputs[0], PrincipledBSDF.outputs[0])

            Object.active_material = Mat

        except:
            bpy.ops.wm.call_menu(name=ErrorMenuNoObjectSelected.bl_idname)

    def OxidizedThoriumShaderAdder(context):

        try:
            MatName = "Oxidized Thorium"
            # Test if material exists
            # If it does not exist, create it:
            Mat = (bpy.data.materials.get(MatName) or
                   bpy.data.materials.new(MatName))

            # Enable 'Use nodes':
            Mat.use_nodes = True
            Nodes = Mat.node_tree.nodes
            Object = bpy.context.active_object

            for node in Nodes:
                Nodes.remove(node)

            # Add a diffuse shader and set its location:
            PrincipledBSDF = Nodes.new('ShaderNodeBsdfPrincipled')
            PrincipledBSDF.location = (100,100)
            PrincipledBSDF.inputs['Base Color'].default_value = (0.036, 0.036, 0.036, 1)
            PrincipledBSDF.inputs['Metallic'].default_value = 1
            PrincipledBSDF.inputs['Roughness'].default_value = 0.709

            Bump = Nodes.new('ShaderNodeBump')
            Bump.location = (-100, 100)
            Bump.inputs['Strength'].default_value = 0.150

            NoiseTexture = Nodes.new('ShaderNodeTexNoise')
            NoiseTexture.location =  (-325, 100)
            NoiseTexture.inputs['Scale'].default_value = 100.000
            NoiseTexture.inputs['Detail'].default_value = 0.500

            MaterialOutput = Nodes.new('ShaderNodeOutputMaterial')
            MaterialOutput.location = (525, 100)

            Mat.node_tree.links.new(Bump.inputs[2], NoiseTexture.outputs[0])
            Mat.node_tree.links.new(PrincipledBSDF.inputs[-3], Bump.outputs[0])
            Mat.node_tree.links.new(MaterialOutput.inputs[0], PrincipledBSDF.outputs[0])

            Object.active_material = Mat

        except:
            bpy.ops.wm.call_menu(name=ErrorMenuNoObjectSelected.bl_idname)

    def WaterShaderAdder(context):

        try:
            MatName = "Water"
            # Test if material exists
            # If it does not exist, create it:
            Mat = (bpy.data.materials.get(MatName) or
                   bpy.data.materials.new(MatName))

            # Enable 'Use nodes':
            Mat.use_nodes = True
            Nodes = Mat.node_tree.nodes
            Object = bpy.context.active_object

            for node in Nodes:
                Nodes.remove(node)

            # Add a diffuse shader and set its location:
            GlassBSDF = Nodes.new('ShaderNodeBsdfGlass')
            GlassBSDF.location = (100,100)
            GlassBSDF.inputs['IOR'].default_value = 1.325

            Bump = Nodes.new('ShaderNodeBump')
            Bump.location = (-125, 100)

            MagicTexture = Nodes.new('ShaderNodeTexMagic')
            MagicTexture.location =  (-350, 100)

            MaterialOutput = Nodes.new('ShaderNodeOutputMaterial')
            MaterialOutput.location = (325, 100)

            Mat.node_tree.links.new(Bump.inputs[2], MagicTexture.outputs[1])
            Mat.node_tree.links.new(GlassBSDF.inputs[3], Bump.outputs[0])
            Mat.node_tree.links.new(MaterialOutput.inputs[0], GlassBSDF.outputs[0])

            Object.active_material = Mat

        except:
            bpy.ops.wm.call_menu(name=ErrorMenuNoObjectSelected.bl_idname)

    def EEVEEGlassShaderSetup(context):

        try:
            MatName = "EEVEE Glass"
            # Test if material exists
            # If it does not exist, create it:
            Mat = (bpy.data.materials.get(MatName) or
                   bpy.data.materials.new(MatName))

            # Enable 'Use nodes':
            Mat.use_nodes = True
            Nodes = Mat.node_tree.nodes
            Object = bpy.context.active_object

            for node in Nodes:
                Nodes.remove(node)

            PrincipledBSDF = Nodes.new('ShaderNodeBsdfPrincipled')
            PrincipledBSDF.location = (100,100)
            PrincipledBSDF.inputs["Roughness"].default_value = 0.0
            PrincipledBSDF.inputs["Transmission"].default_value = 1.0

            MaterialOutput = Nodes.new('ShaderNodeOutputMaterial')
            MaterialOutput.location = (525, 100)

            Mat.node_tree.links.new(MaterialOutput.inputs[0], PrincipledBSDF.outputs[0])

            Object.active_material = Mat

            bpy.context.scene.eevee.use_ssr = True
            bpy.context.scene.eevee.use_ssr_refraction = True
            Object.active_material.use_screen_refraction = True

        except:
            bpy.ops.wm.call_menu(name=ErrorMenuNoObjectSelected.bl_idname)

    def GradientAdder(context):

        try:
            MatName = "Gradient"
            # Test if material exists
            # If it does not exist, create it:
            Mat = (bpy.data.materials.get(MatName) or
                   bpy.data.materials.new(MatName))

            # Enable 'Use nodes':
            Mat.use_nodes = True
            Nodes = Mat.node_tree.nodes
            Object = bpy.context.active_object

            for node in Nodes:
                Nodes.remove(node)

            # Add a diffuse shader and set its location:
            TextureCoordinate = Nodes.new('ShaderNodeTexCoord')
            TextureCoordinate.location = (100,100)

            Mapping = Nodes.new('ShaderNodeMapping')
            Mapping.location = (325,100)

            SeparateXYZ = Nodes.new('ShaderNodeSeparateXYZ')
            SeparateXYZ.location = (550, 100)

            ColorRamp = Nodes.new('ShaderNodeValToRGB')
            ColorRamp.location = (875, 100)

            MaterialOutput = Nodes.new('ShaderNodeOutputMaterial')
            MaterialOutput.location = (1100, 100)

            Mat.node_tree.links.new(Mapping.inputs[0], TextureCoordinate.outputs[0])
            Mat.node_tree.links.new(SeparateXYZ.inputs[0], Mapping.outputs[0])
            Mat.node_tree.links.new(ColorRamp.inputs[0], Mapping.outputs[0])
            Mat.node_tree.links.new(MaterialOutput.inputs[0], ColorRamp.outputs[0])

            bpy.data.materials["Gradient"].node_tree.nodes["ColorRamp"].label = "ColorRamp/Use it to modify the Gradient"

            Object.active_material = Mat

        except:
            bpy.ops.wm.call_menu(name=ErrorMenuNoObjectSelected.bl_idname)

    def FogAdder(context):
        
        try:
            MatName = "Fog"

            Mat = (bpy.data.materials.get(MatName) or 
                   bpy.data.materials.new(MatName))

            Mat.use_nodes = True
            Nodes = Mat.node_tree.nodes
            Object = bpy.context.active_object

            for node in Nodes:
                Nodes.remove(node)

            Emission = Nodes.new('ShaderNodeEmission')
            Emission.location = (100, 100)

            MaterialOutput = Nodes.new('ShaderNodeOutputMaterial')
            MaterialOutput.location = (325, 100)

            Mat.node_tree.links.new(MaterialOutput.inputs[1], Emission.outputs[0])

            Object.active_material = Mat
        
        except:
            bpy.ops.wm.call_menu(name=ErrorMenuNoObjectSelected.bl_idname)

    def RainbowFogAdder(context):
        
        try:
            MatName = "Rainbow Fog"

            Mat = (bpy.data.materials.get(MatName) or 
                   bpy.data.materials.new(MatName))

            Mat.use_nodes = True
            Nodes = Mat.node_tree.nodes
            Object = bpy.context.active_object

            for node in Nodes:
                Nodes.remove(node)

            TextureCoordinate = Nodes.new('ShaderNodeTexCoord')
            TextureCoordinate.location = (100, 100)

            MaterialOutput = Nodes.new('ShaderNodeOutputMaterial')
            MaterialOutput.location = (325, 100)

            Mat.node_tree.links.new(MaterialOutput.inputs[1], TextureCoordinate.outputs[0])

            Object.active_material = Mat
        
        except:
            bpy.ops.wm.call_menu(name=ErrorMenuNoObjectSelected.bl_idname)

    def SkinVertexSetup(context):

        bpy.ops.mesh.primitive_vert_add()

        Object = bpy.context.active_object
        Mod = Object.modifiers.new("Skin", "SKIN")

    def EEVEEReflectionsSetup(context):

        Object = bpy.context.active_object

        bpy.context.scene.eevee.use_gtao = True
        bpy.context.scene.eevee.use_bloom = True
        bpy.context.scene.eevee.use_ssr = True

        try:
            Object.active_material.use_screen_refraction = True

            if Object.active_material.use_screen_refraction == True:
                bpy.ops.wm.call_menu(name=MenuObjectAlreadyHasReflections.bl_idname)

        except:
            bpy.ops.wm.call_menu(name=ErrorMenuNoObjectSelectedB.bl_idname)


class SceneCreator(bpy.types.Operator):
    """Creates a three plane basic scene"""
    bl_idname = "object.scene_creator"
    bl_label = "Basic Scene Creator"

    def execute(self, context):
        CoreFunctions.SimpleSceneAdder(context)
        return {'FINISHED'}

class DefaultCubeDeleter(bpy.types.Operator):
    """Deletes the default cube or just a cube"""
    bl_idname = "object.delete_dflt_cube"
    bl_label = "Delete Default Cube"

    def execute(self, context):
        CoreFunctions.DefCubeDel(context)
        return {'FINISHED'}

class BasicToonShaderAdder(bpy.types.Operator):
    """Adds a basic toon shader to the selected mesh (EEVEE only)"""
    bl_idname = "object.basic_toon_shader_add"
    bl_label = "Basic Toon Shader Adder"

    def execute(self, context):
        CoreFunctions.BasicToonShaderAdder(context)
        return {'FINISHED'}

class CopperShaderAdder(bpy.types.Operator):
    """Adds a copper shader to the selected mesh (Cycles only)"""
    bl_idname = "object.copper_shader_add"
    bl_label = "Copper Shader Adder"

    def execute(self, context):
        CoreFunctions.CopperShaderAdder(context)
        return {'FINISHED'}

class RedCopperShaderAdder(bpy.types.Operator):
    """Adds a red copper shader to the selected mesh (Cycles only)"""
    bl_idname = "object.red_copper_shader_add"
    bl_label = "Red Copper Shader Adder"

    def execute(self, context):
        CoreFunctions.RedCopperShaderAdder(context)
        return {'FINISHED'}

class UnpolishedAluminumShaderAdder(bpy.types.Operator):
    """Adds an unpolished aluminum shader to the selected mesh (Cycles only)"""
    bl_idname = "object.unpolished_aluminum_shader_add"
    bl_label = "Unpolished Aluminum Shader Adder"

    def execute(self, context):
        CoreFunctions.UnpolishedAluminumShaderAdder(context)
        return {'FINISHED'}

class OxidizedThoriumShaderAdder(bpy.types.Operator):
    """Adds an oxidized thorium shader to the selected mesh (Cycles only)"""
    bl_idname = "object.oxidized_thorium_shader_add"
    bl_label = "Oxidized Thorium Shader Adder"

    def execute(self, context):
        CoreFunctions.OxidizedThoriumShaderAdder(context)
        return {'FINISHED'}

class WaterShaderAdder(bpy.types.Operator):
    """Adds a water shader to the select mesh (Cycles only)"""
    bl_idname = "object.water_shader_add"
    bl_label = "Water Shader Adder"

    def execute(self, context):
        CoreFunctions.WaterShaderAdder(context)
        return {'FINISHED'}

class EEVEEGlassShaderSetup(bpy.types.Operator):
    """Adds a Glass shader to the select mesh (EEVEE only)"""
    bl_idname = "object.eevee_glass_shader_setup"
    bl_label = "EEVEE Glass Shader Setup"

    def execute(self, context):
        CoreFunctions.EEVEEGlassShaderSetup(context)
        return {'FINISHED'}

class GradientAdder(bpy.types.Operator):
    """Adds a gradient to the select mesh"""
    bl_idname = "object.gradient_add"
    bl_label = "Gradient Adder"

    def execute(self, context):
        CoreFunctions.GradientAdder(context)
        return {'FINISHED'}

class FogAdder(bpy.types.Operator):
    """Adds a fog shader to the select mesh"""
    bl_idname = "object.fog_add"
    bl_label = "Fog Adder"

    def execute(self, context):
        CoreFunctions.FogAdder(context)
        return {'FINISHED'}

class RainbowFogAdder(bpy.types.Operator):
    """Adds a rainbow fog shader to the select mesh"""
    bl_idname = "object.rainbow_fog_add"
    bl_label = "Rainbow Fog Adder"

    def execute(self, context):
        CoreFunctions.RainbowFogAdder(context)
        return {'FINISHED'}

class SkinVertexSetup(bpy.types.Operator):
    """Adds a single Vertex and makes it so it has a skin modifier"""
    bl_idname = "object.skin_vertex_setup"
    bl_label = "Skin Vertex Setup"

    def execute(self, context):
        CoreFunctions.SkinVertexSetup(context)
        return {'FINISHED'}

class EEVEEReflectionsSetup(bpy.types.Operator):
    """Puts all prepared for reflections in EEVEE"""
    bl_idname = "object.eevee_reflections_setup"
    bl_label = "EEVEE Reflections Setup"

    def execute(self, context):
        CoreFunctions.EEVEEReflectionsSetup(context)
        return {'FINISHED'}



# def menu_func(self, context):
#     self.layout.operator(SimpleOperator.bl_idname, text=SimpleOperator.bl_label)




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
        layout.label(text="Scene:")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.scene_creator")

        # Delete Default Cube Button
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.delete_dflt_cube")

        # Adds Basic Toon Shader Button
        layout.label(text="Shaders:")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.basic_toon_shader_add")

        # Adds Copper Shader Button
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.copper_shader_add")

        # Adds Red Copper Shader Button
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.red_copper_shader_add")

        # Adds Unpolished Aluminum Shader Button
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.unpolished_aluminum_shader_add")

        # Add Oxidized Thorium Shader Button
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.oxidized_thorium_shader_add")

        # Add Water Shader Button
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.water_shader_add")

        # Add Gradient Button
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.gradient_add")

        # Add EEVEE Glass Shader Setup Button
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.eevee_glass_shader_setup")

        # Add Fog Shader Button
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.fog_add")

        # Add Rainbow Fog Shader Button
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.rainbow_fog_add")

        # Add Skin Vertex Setup Button
        layout.label(text="Misc")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.skin_vertex_setup")
        
        # EEVEE Reflections Setup Button
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.eevee_reflections_setup")



def register():
    bpy.utils.register_class(ErrorMenuNoCubes)
    bpy.utils.register_class(ErrorMenuNoObjectSelected)
    bpy.utils.register_class(ErrorMenuNoObjectSelectedB)
    bpy.utils.register_class(MenuObjectAlreadyHasReflections)

    bpy.utils.register_class(RainbowFogAdder)
    bpy.utils.register_class(EEVEEReflectionsSetup)
    bpy.utils.register_class(FogAdder)
    bpy.utils.register_class(EEVEEGlassShaderSetup)
    bpy.utils.register_class(SkinVertexSetup)
    bpy.utils.register_class(GradientAdder)
    bpy.utils.register_class(WaterShaderAdder)
    bpy.utils.register_class(OxidizedThoriumShaderAdder)
    bpy.utils.register_class(UnpolishedAluminumShaderAdder)
    bpy.utils.register_class(RedCopperShaderAdder)
    bpy.utils.register_class(CopperShaderAdder)
    bpy.utils.register_class(BasicToonShaderAdder)
    bpy.utils.register_class(DefaultCubeDeleter)
    bpy.utils.register_class(SceneCreator)
    # bpy.types.VIEW3D_MT_object.append(menu_func)
    bpy.utils.register_class(LayoutDemoPanel)


def unregister():
    bpy.utils.unregister_class(ErrorMenuNoCubes)
    bpy.utils.unregister_class(ErrorMenuNoObjectSelected)
    bpy.utils.unregister_class(ErrorMenuNoObjectSelectedB)
    bpy.utils.unregister_class(MenuObjectAlreadyHasReflections)

    bpy.utils.unregister_class(RainbowFogAdder)
    bpy.utils.unregister_class(EEVEEReflectionsSetup)
    bpy.utils.unregister_class(FogAdder)
    bpy.utils.unregister_class(EEVEEGlassShaderSetup)
    bpy.utils.unregister_class(SkinVertexSetup)
    bpy.utils.unregister_class(GradientAdder)
    bpy.utils.unregister_class(WaterShaderAdder)
    bpy.utils.unregister_class(OxidizedThoriumShaderAdder)
    bpy.utils.unregister_class(UnpolishedAluminumShaderAdder)
    bpy.utils.unregister_class(RedCopperShaderAdder)
    bpy.utils.unregister_class(CopperShaderAdder)
    bpy.utils.unregister_class(BasicToonShaderAdder)
    bpy.utils.unregister_class(DefaultCubeDeleter)
    bpy.utils.unregister_class(LayoutDemoPanel)
    bpy.utils.unregister_class(SceneCreator)
    # bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()
