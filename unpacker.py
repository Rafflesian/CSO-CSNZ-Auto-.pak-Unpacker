import subprocess;
from pathlib import Path;

def fnParseDirectory(szPrompt: str, szSuffix: str = ""):
    
    szSuffix = szSuffix.replace(" ", "").lower();

    if(szSuffix):
        szPrompt += f" ({szSuffix})";

    szPrompt += ": ";

    while True:

        szReturn = input(szPrompt).replace("\"", "");
        pPath = Path(szReturn);

        if(not pPath.exists()):
            print(f"Invalid directory '{szReturn}'");
            continue;
        
        if(szSuffix):

            if(not pPath.is_file()):
                print(f"Provided route is not an '{szSuffix}' file");
                continue;
        
            if(pPath.suffix.lower() != szSuffix):
                print(f"Provided file doesn't match suffix '{szSuffix}'");
                continue;
        else:

            if(not pPath.is_dir()):
                print("Provided route is not a directory");
                continue;
        
        break;

    return szReturn;

szUnpacker  = fnParseDirectory("Unpacker Route", '.exe');
szPack      = fnParseDirectory(".pak Route");
szOutput    = fnParseDirectory("Output Route");

iFileCount = 0;

while True:

    szFile = f"common_{'{:0>5}'.format(iFileCount)}.pak";
    szFilePath = f"{szPack}/{szFile}";

    if(not Path(szFilePath).exists()):
        break;

    print(f"Processing: {szFilePath}");
    subprocess.run([szUnpacker, szFilePath], cwd=szOutput, check = True);

    iFileCount += 1;

if(iFileCount):
    print(f"{iFileCount} files processed");
else:
    print("No .pak files were found");