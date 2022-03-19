# coding=utf-8
# enconding = utf-8
# ConfigParser模块在python3中修改为configparser.这个模块定义了一个ConfigParser类，该类的作用是使用配置文件生效，配置文件的格式和windows的INI文件的格式相同
from configparser import configparser
from projectVar.Var import page_object_path


# 读取.ini配置文件

class ParsePageObject(object):
    def __init__(self):
        # self.cf=ConfigParser()
        self.cf.read(page_object_path)  # page_object_repository_path是配置文件的路径

    def getItemsFromSection(self, sectionName):
        # print self.cf.items(sectionName)
        return dict(self.cf.items(sectionName))

    # 获取某一个具体的选项对应的value
    def getOptionValue(self, sectionName, optionName):
        return self.cf.get(sectionName, optionName)


if __name__ == '__main__':
    pp = ParsePageObject()
    print(pp.getItemsFromSection("Vizlauncher_login"))
