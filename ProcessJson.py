import os
def RemoveShaderCode(variantList):
    for variant in variantList:
        if 'shaderCodes' in variant and isinstance(variant['shaderCodes'], list):
            # 创建一个新的列表来存储不包含 "platformName": "ESSL_310" 的 shaderCode
            variant['shaderCodes'] = [code for code in variant['shaderCodes'] if not (
                'platformShaderStage' in code and
                'platformName' in code['platformShaderStage'] and
                code['platformShaderStage']['platformName'] == 'ESSL_310'
            )]

def ProcessWorkdir(workdir):
    jsonPaths = []
    for root, dirs, files in os.walk(workdir):
        # 容易发现，需要处理的json所在的目录下都没有子目录了
        if not dirs: # 因此，只要发现还有子目录，就继续往下深入
            for file in files:
                if file.endswith(".json"):
                    jsonPath = os.path.join(root, file)
                    jsonPaths.append(jsonPath)
    return jsonPaths

def DelSpecificFile(workdir):
    for root, dirs, files in os.walk(workdir):
        for file in files:
            if "ESSL_310" in file:
                filePath = os.path.join(root, file)
                os.remove(filePath)
                print(f"Deleted: {filePath}")