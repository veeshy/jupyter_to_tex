# jupyter_to_tex
A script to convert Jupiter notebook markdown outputs into latex source code

## Details
There is no simple way to export latex (.tex) source code from jupyter notebooks. PDFs can be exported via latex but often you do not want the python code and you want to let your latex code handle the formatting (e.g., your own style package). To get latex code, the jupter notebook should be exported to markdown (.md) then passed to the python code remover here. If you want all the python code in the final tex file, skip the the end of the Usage section below.

## Usage
* Export the jupyter notebook as markdown (.md)
* Run the python script:

  > python remove_py_md.py path_to_md.md
  
  > output: path_to_md_no_py.md
* Run pandocs on this outputted .md file. ( --wrap=preserve keeps spacing of the original markdown)

  > pandoc --listings -f markdown -t latex path_to_md_no_py.md -o tex_output.tex  --wrap=preserve
  
## Requires
* pandocs (comes with the anaconda stack)

## Limitations
The tex code created is meant to be imported via an \include{} statement, or copying and pasting into working tex files (i.e., there is no latex boilerplate code in the pandocs output)

The tex code will still likely need some cleaning up but it's still a rather nice workflow.
