import bpy


bl_info = {
    "name": "Utilidades Varias",
    "author": "Electrofer",
    "version": (0, 4, 5, 1),
    "blender": (2, 80, 0),
    "location": "En el menu de propiedades de la escena",
    "description": "Hace tu vida un poco mas facil",
    "warning": "En desarrollo, bugs pueden ocurrir",
    "doc_url": "",
    "category": "Utilidades",
}


class ErrorMenuNoCubes(bpy.types.Menu):
    bl_label = "Ha ocurrido un error"
    bl_idname = "error_menu_no_cubes"

    def draw(self, context):
        layout = self.layout

        layout.label(text="No hay cubos en la escena.")

class ErrorMenuNoObjectSelected(bpy.types.Menu):
    bl_label = "Ha ocurrido un error"
    bl_idname = "error_menu_no_object_selected"

    def draw(self, context):
        layout = self.layout

        layout.label(text="No hay objetos seleccionados a los que aplicarles el Shader.")

class ErrorMenuNoObjectSelectedB(bpy.types.Menu):
    bl_label = "Algo no ha podido ser resuelto"
    bl_idname = "error_menu_no_object_selected_b"

    def draw(self, context):
        layout = self.layout

        layout.label(text="No hay ningun objeto seleccionado. Para hacer la accion entera, por favor selecciona un objeto.")

class MenuObjectAlreadyHasReflections(bpy.types.Menu):
    bl_label = "Algo ha salido mal"
    bl_idname = "menu_object_already_has_reflections"

    def draw(self, context):
        layout = self.layout

        layout.label(text="Este objeto ya tiene reflexiones")




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
            MatName = "Toon Shader Basico"
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

            bpy.data.materials["Toon Shader Basico"].node_tree.nodes["ColorRamp"].label = "ColorRamp/Usalo para modificar el shader"

            Object.active_material = Mat

        except:
            bpy.ops.wm.call_menu(name=ErrorMenuNoObjectSelected.bl_idname)

    def CopperShaderAdder(context):

        try:
            MatName = "Cobre"
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
            MatName = "Cobre Rojo"
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
            MatName = "Aluminio Sin Pulir"
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
            MatName = "Torio Oxidado"
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
            MatName = "Agua"
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
            MatName = "Vidrio EEVEE"
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
            MatName = "Gradiente"
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

            bpy.data.materials["Gradiente"].node_tree.nodes["ColorRamp"].label = "ColorRamp/Usalo para modificar el Gradiente"

            Object.active_material = Mat

        except:
            bpy.ops.wm.call_menu(name=ErrorMenuNoObjectSelected.bl_idname)

    def FogAdder(context):
        
        try:
            MatName = "Niebla"

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
            MatName = "Niebla Arcoiris"

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
    """Crea una simple escena de tres planos"""
    bl_idname = "object.scene_creator"
    bl_label = "Creador de Escenas Basico"

    def execute(self, context):
        CoreFunctions.SimpleSceneAdder(context)
        return {'FINISHED'}

class DefaultCubeDeleter(bpy.types.Operator):
    """Elimina el cubo por defecto o simplemente un cubo"""
    bl_idname = "object.delete_dflt_cube"
    bl_label = "Elimina Cubo por Defecto"

    def execute(self, context):
        CoreFunctions.DefCubeDel(context)
        return {'FINISHED'}

class BasicToonShaderAdder(bpy.types.Operator):
    """Añade un toon shader basico a el objeto seleccionado (solo EEVEE)"""
    bl_idname = "object.basic_toon_shader_add"
    bl_label = "Añadidor de un Toon Shader Basico"

    def execute(self, context):
        CoreFunctions.BasicToonShaderAdder(context)
        return {'FINISHED'}

class CopperShaderAdder(bpy.types.Operator):
    """Añade un shader de cobre a el objeto seleccionado"""
    bl_idname = "object.copper_shader_add"
    bl_label = "Añadidor de Shader Cobre"

    def execute(self, context):
        CoreFunctions.CopperShaderAdder(context)
        return {'FINISHED'}

class RedCopperShaderAdder(bpy.types.Operator):
    """Añade un shader de cobre rojo a el objeto seleccionado"""
    bl_idname = "object.red_copper_shader_add"
    bl_label = "Añadidor de Shader Cobre Rojo"

    def execute(self, context):
        CoreFunctions.RedCopperShaderAdder(context)
        return {'FINISHED'}

class UnpolishedAluminumShaderAdder(bpy.types.Operator):
    """Añade un shader de aluminio sin pulir a el objeto seleccionado"""
    bl_idname = "object.unpolished_aluminum_shader_add"
    bl_label = "Añadidor de Shader Aluminio Sin Pulir"

    def execute(self, context):
        CoreFunctions.UnpolishedAluminumShaderAdder(context)
        return {'FINISHED'}

class OxidizedThoriumShaderAdder(bpy.types.Operator):
    """Añade un shader de torio oxidado a el objeto seleccionado"""
    bl_idname = "object.oxidized_thorium_shader_add"
    bl_label = "Añadidor de Shader Torio Oxidado"

    def execute(self, context):
        CoreFunctions.OxidizedThoriumShaderAdder(context)
        return {'FINISHED'}

class WaterShaderAdder(bpy.types.Operator):
    """Añade un shader de agua a el objeto seleccionado"""
    bl_idname = "object.water_shader_add"
    bl_label = "Añadidor de Shader Agua"

    def execute(self, context):
        CoreFunctions.WaterShaderAdder(context)
        return {'FINISHED'}

class EEVEEGlassShaderSetup(bpy.types.Operator):
    """Añade un shader de vidrio a el objeto seleccionado (solo EEVEE)"""
    bl_idname = "object.eevee_glass_shader_setup"
    bl_label = "Añadidor de Shader Vidrio"

    def execute(self, context):
        CoreFunctions.EEVEEGlassShaderSetup(context)
        return {'FINISHED'}

class GradientAdder(bpy.types.Operator):
    """Añade un gradiente a el objeto seleccionado"""
    bl_idname = "object.gradient_add"
    bl_label = "Añadidor de Gradiente"

    def execute(self, context):
        CoreFunctions.GradientAdder(context)
        return {'FINISHED'}

class FogAdder(bpy.types.Operator):
    """Añade un shader de niebla al objeto seleccionado"""
    bl_idname = "object.fog_add"
    bl_label = "Añadidor de Niebla"

    def execute(self, context):
        CoreFunctions.FogAdder(context)
        return {'FINISHED'}

class RainbowFogAdder(bpy.types.Operator):
    """Añade un shader de niebla arcoiris al objeto seleccionado"""
    bl_idname = "object.rainbow_fog_add"
    bl_label = "Añadidor de Niebla Arcoiris"

    def execute(self, context):
        CoreFunctions.RainbowFogAdder(context)
        return {'FINISHED'}


class SkinVertexSetup(bpy.types.Operator):
    """Añade un vertice y le pone un modificador de skin"""
    bl_idname = "object.skin_vertex_setup"
    bl_label = "Skin Vertex Setup"

    def execute(self, context):
        CoreFunctions.SkinVertexSetup(context)
        return {'FINISHED'}

class EEVEEReflectionsSetup(bpy.types.Operator):
    """Pone todo preparado para reflexiones en EEVEE"""
    bl_idname = "object.eevee_reflections_setup"
    bl_label = "Setup Reflexiones de EEVEE"

    def execute(self, context):
        CoreFunctions.EEVEEReflectionsSetup(context)
        return {'FINISHED'}

# def menu_func(self, context):
#     self.layout.operator(SimpleOperator.bl_idname, text=SimpleOperator.bl_label)




class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Utilidades Varias"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Scene button
        layout.label(text="Escena:")
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

        # Add EEVEE Glass Shader Setup
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
