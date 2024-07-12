import json
import ProcessJson

InputDir = input("Workdir: ")

jsonPaths = ProcessJson.ProcessWorkdir(InputDir)
for path in jsonPaths:
    print(path)
    with open(path, "r", encoding="utf-8") as ToBeProcessed:
        data = json.load(ToBeProcessed)
        if 'variantList' in data and isinstance(data['variantList'], list):
            ProcessJson.RemoveShaderCode(data['variantList'])
        with open(path, "w", encoding = "utf-8") as OutputWriteBack:
            json.dump(data, OutputWriteBack, ensure_ascii = False, indent = 2)


ProcessJson.DelSpecificFile(InputDir)