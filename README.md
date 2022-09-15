# rene_warnings

Warchart won't work in families

I did prototype a quick tool to do what you need.

Just get the content of the zip file ( https://github.com/jmcouffin/rene_warnings/blob/a1aaab0e77c162e51fe9da230cd183170dc3b4bc/Warnings.pushbutton.zip )in a folder like this one in your pyrevit install (implies you have pyRevit):

%AppData%\Roaming\pyRevit-Master\extensions\pyRevitTools.extension\http://pyRevit.tab\Project.panel\ptools.stack\Family.pulldown

you might have to remove the bundle.yaml of the higher level folder you see in this picture for it to show up
![image](https://user-images.githubusercontent.com/7872003/190349396-c191ae47-8a67-470c-9922-6e3605a64923.png)


after that, use the reload button in pyRevit and you should find the tool under pyRevit, Project, Family pulldown
