import os
total=0
def file_size(path):
    total=os.path.getsize(path)
    if os.path.isdir(path):
        for item in os.listdir(path):
            child_path=os.path.join(path,item)
            total+=file_size(child_path)
    return total

path='/Users/harshavardanmanam/Documents/ds_algo_in_python/Chapter1'
print(os.path.isdir(path))
print(os.path.getsize(path))
print(os.listdir(path))
print(file_size(path))