import audio_metadata
import pandas as pd
import sys 

def extract_metadata(filepath):
    metadata = audio_metadata.load(filepath)
    df = pd.DataFrame.from_dict({ key:["&".join(value) if type(value[0])==str else None] for key,value in metadata.tags.items()})
    return df

def generate_array(filepaths,save_path="file.csv"):
    try:
        df = pd.concat([extract_metadata(filepath) for filepath in filepaths])
        df.to_csv(save_path)
        print("Save in {}".format(save_path))
        return True
    except Exception as ex:
        print("Not saved due to an ERROR")
        print(ex)
        return False

def main(argv):
    return generate_array(argv)

if __name__== "__main__":
   
    main(sys.argv[1:])


