
from directory_tree import display_tree
import json
import os;

def main2():
    folder = '/Users/qianli/workspace/python/www/tools/1661068531010/LeAuth-new'
    filepaths = [os.path.join(folder, f) for f in os.listdir(folder)]
    print(filepaths)
    filepaths = [f.path for f in os.scandir(folder) if f.is_file()]
    dirpaths = [f.path for f in os.scandir(folder) if f.is_dir()]
    print(filepaths)
    print(dirpaths)

    jsonS = [];
    # jsonS["text"]="LeAuth-new";
    jsonS.append({"text":"LeAuth-new","icon": "fa fa-folder","node":[]})
    for i in dirpaths:
        jsonS[0]["nodes"].append({"text":i,"icon": "fa fa-folder"});
    for i in filepaths:
        jsonS[0]["nodes"].append({"text":i,"icon": "fa fa-folder"});
    print(jsonS)

def main1():
    rootDir = '/Users/qianli/workspace/python/www/tools/1661068531010/LeAuth-new'
    for dirName, subdirList, fileList in os.walk(rootDir):
        print('path directory=%s,directory name=%s' % (dirName,getEndFileName((dirName))))
    for fname in fileList:
        print('path=%s,filename=%s' % (fname,getEndFileName(fname)))

def main4():
    jsonS = [];
    jsonS.append({"id": 0, "text": "LeAuth-new", "selectedIcon": "glyphicon glyphicon-ok",
                  "color": "#ff0000",
                  "icon": "glyphicon glyphicon-play-circle", "nodes": []})

    rootDir = '/Users/qianli/workspace/python/www/tools/1661068531010/LeAuth-new'

    jsonList=[];
    for root, dirs, files in os.walk(rootDir, topdown=False):
        jsonTemp=[];
        # print(root)
        for name in dirs:
            tmpPath=os.path.join(root, name);
            # print(tmpPath)
            jsonTemp.append({"id":tmpPath,"text":name});
        for name in files:
            tmpPath = os.path.join(root, name);
            # print(tmpPath)
            jsonTemp.append({"id": tmpPath, "text": name});
        jsonList.append(jsonTemp);
        if len(jsonList)>0:
            jsonListEnd=[];
            jsonName=getEndFileName(root);
            jsonListEnd.append({"id": root, "text": jsonName[0], "nodes": []});
            jsonListEnd[0]["nodes"].append(jsonList);
            jsonList = jsonListEnd;
        # print(name)
        # jsonS[0]["nodes"].append({"id": i, "text": getEndFileName(i), "nodes": [{"id": "test", "text": "test"}]});
        # for name in root:
        #     print(name);



        # for name in decompiler:
            # print(os.path.join(root, name))
            # print(name)
    print(jsonList)

def getEndFileName(fileName):
    fileName = fileName.split("/");
    return fileName[len(fileName)-1:len(fileName)];

def main():
    localPath = '/Users/qianli/workspace/python/www/tools/1661068531010/LeAuth-new';
    res = display_tree(localPath,True)
    resLine = res.splitlines();
    endJson=[];
    endJson['text'] = resLine[0];
    for i in resLine:

        print(i)


if __name__ == '__main__':
    main4()


