# 计算性函数库

def get_file_type(file_name): # 返回文件后缀名，并全部转成小写
    return file_name.split(".")[-1].lower()

def has_prefix(s_var, s_pre): # 检查 s_pre 是不是 s_var 的前缀
    if(s_pre[-1] == '$'):    # 精确匹配
        s_tmp = s_pre[:-1]
        return s_var == s_tmp
    elif len(s_var) < len(s_pre):
        return False
    return s_var[:len(s_pre)] == s_pre # 截取 s_var 的前若干个字符进行匹配
