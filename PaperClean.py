import os
import re
import shutil
def parse(tex_dir,tex_path,dependent_files,remove_comments,merge_tex):
    """Parse the tex file and copy all the dependent files to the output directory"""

    with open(os.path.join(tex_dir,tex_path),"r",encoding="utf8") as f:
        tex_str=f.read()
    if remove_comments:
        # remove \begin{comment}\n xxx \n\end{comment} 
        tex_str=re.sub(r"\\begin{comment}.*?\\end{comment}", "", tex_str, flags=re.DOTALL)
        # remove % xxx at the beginning of the line
        tex_str = re.sub(r"(?m)^%.*\n?", "", tex_str)
        # remove % xxx at the end of the line
        tex_str=re.sub(r"(?<!\\)%.*", "", tex_str, flags=re.MULTILINE)
    
    # depend \includegraphics...{xxx}
    includegraphics_pattern = re.compile(r'\\includegraphics.*?\{(.+?)\}')
    matches = includegraphics_pattern.findall(tex_str)
    for match in matches:
        dependent_files.append(match)
    
    # find \input{xxx} and parse the input file
    input_pattern = re.compile(r'\\input\{(.+?)\}')
    matches = input_pattern.findall(tex_str)
    for match in matches:
        input_tex_path = match
        if merge_tex==False:
            dependent_files.append(input_tex_path)
        else:
            input_tex_str = parse(tex_dir, input_tex_path, dependent_files, remove_comments, merge_tex)
            tex_str = tex_str.replace(f'\\input{{{input_tex_path}}}', input_tex_str)
    
    return tex_str

def parse_main(main_tex_path,output_dir,retain_file_extensions_list,remove_comments=True,merge_tex=True):
    """Parse the main tex file and copy all the dependent files to the output directory"""
    tex_dir=os.path.dirname(main_tex_path)
    main_tex_name=os.path.basename(main_tex_path)
    dependent_files=[filename for filename in os.listdir(tex_dir) if any(filename.endswith(extension) for extension in retain_file_extensions_list)]
    
    tex_str=parse(tex_dir,main_tex_name,dependent_files,remove_comments,merge_tex)
    
    # fix the block of author and affiliations
    def fix_block(block):
        return re.sub(r'\n\s*\n', '\n', block)

    tex_str = re.sub(r'(\\author{.*?})', lambda m: fix_block(m.group(1)), tex_str, flags=re.DOTALL)
    tex_str = re.sub(r'(\\affiliations{.*?})', lambda m: fix_block(m.group(1)), tex_str, flags=re.DOTALL)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in dependent_files:
        src=os.path.join(tex_dir,filename)
        dst=os.path.join(output_dir,filename)
        dst_dir=os.path.dirname(dst)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        shutil.copy2(src,dst_dir)
    if merge_tex:
        with open(os.path.join(output_dir,main_tex_name),"w",encoding="utf8") as f:
            f.write(tex_str)


from config import *
if __name__=="__main__":
    main_tex_path=os.path.join(tex_dir,main_tex_name)

    parse_main(main_tex_path,output_dir=output_dir,retain_file_extensions_list=retain_file_extensions_list,remove_comments=remove_comments,merge_tex=merge_tex)