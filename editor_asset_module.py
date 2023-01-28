"""
编辑器资源操作工具类 整理一些常用的方法进行封装
"""
import unreal
EditorAssetLibrary = unreal.EditorAssetLibrary
EditorUtilityLibrary = unreal.EditorUtilityLibrary
EditorDialog = unreal.EditorDialog
toolMenus = unreal.ToolMenus
ToolMenuEntry = unreal.ToolMenuEntry

'''
==================================操作文件夹相关===================================
'''
#根据文件夹路径返回当前目录下所有asset对象
def list_assetobjs_in_directory(directory_path, recursive=True):
    directory_exist = EditorAssetLibrary.does_directory_exist(directory_path)
    asset_obj_arr = []
    if directory_exist != True:
        EditorDialog.show_message("提示","请检查输入的路径是否存在:"+directory_path,unreal.AppMsgType.OK)
    else:
        obj_paths = EditorAssetLibrary.list_assets(directory_path,recursive)
        for obj_path in obj_paths:
            asset_obj = EditorAssetLibrary.load_asset(obj_path)
            asset_obj_arr.append(asset_obj)
    return asset_obj_arr

#根据类型组过滤asset对象
#如types = (unreal.Texture,unreal.StaticMesh)元组
def filter_assetobjs_by_type(asset_objs,types):
    filter_assetobjs = [asset for asset in asset_objs if isinstance(asset,types)]
    return filter_assetobjs


#根据类型组过滤某个目录的对象
#如types = (unreal.Texture,unreal.StaticMesh)元组
def list_asset_in_directory_by_type(directory_path,types,recursive=True):
    asset_list = list_assetobjs_in_directory(directory_path,recursive)
    filter_asset_list = filter_assetobjs_by_type(asset_list,types)
    return filter_asset_list


'''
=================================按钮相关操作=======================================
'''
#################################关卡编辑器按钮###################################
#获取关卡编辑器主按钮
def find_leveleditor_mainmenu():
    menus = toolMenus.get()
    main_menu = menus.find_menu("LevelEditor.MainMenu")
    return main_menu

#给关卡编辑添加一级子按钮
def leveleditor_mainmenu_add_sub_menu(sub_menu_name):
    main_menu = find_leveleditor_mainmenu()
    main_menu.add_sub_menu(main_menu.get_name(), sub_menu_name, sub_menu_name, sub_menu_name)

#给管卡编辑一级子按钮增加entry按钮
def leveleditor_submenu_add_sub_menu(sub_menu_name,menu_entry_name,menu_entry):
    main_menu = find_leveleditor_mainmenu()
    sub_menu = main_menu.add_sub_menu(main_menu.get_name(), sub_menu_name, sub_menu_name, sub_menu_name)
    sub_menu.add_menu_entry(menu_entry_name,menu_entry)



#################################内容浏览器按钮####################################
#获取内容浏览器文件夹按钮
def find_contentbrowser_folder_menu():
    menus = toolMenus.get()
    main_menu = menus.find_menu("ContentBrowser.FolderContextMenu")
    return main_menu

#获取内容浏览器文件按钮
def find_contentbrowser_asset_menu():
    menus = toolMenus.get()
    main_menu = menus.find_menu("ContentBrowser.AssetContextMenu")
    return main_menu

#向内容浏览文件按钮添加toolmenuenityscript
def contentbrowser_asset_add_menuentryscript(menu_entry_script):
    asset_menu = find_contentbrowser_asset_menu()
    asset_menu.add_menu_entry_object(menu_entry_script)

