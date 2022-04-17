def get_str(file_bytes:bytes)->str:
    file_str = "".join([file_bytes[i:i+1].hex() for i in range(len(file_bytes))])
    return file_str

def get_bytes(file_str:str)->bytes:
    file_str_2_list = [file_str[i:i+2] for i in range(0,len(file_str),2)]
    file_bytes = bytes([int(i,16) for i in file_str_2_list])
    return file_bytes

def read_file(url:str)->bytes:
    with open(url,"rb+") as f:
        return f.read()

def write_file(file_bytes:bytes,url:str)->None:
    with open(url,"wb+") as f:
        f.write(file_bytes)
    return None

if __name__ == "__main__":
    file = read_file(r"hello.png")
    temp = get_bytes(get_str(file))
    write_file(temp,r'new_hello.png')