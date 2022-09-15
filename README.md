# rene_warnings

[Warchart](https://apps.autodesk.com/RVT/en/Detail/Index?id=5069841371205448504&appLang=en&os=Win64) won't work in families

I did prototype a quick tool to do what you need [René](https://twitter.com/BIM4GIB)

![how it works](https://user-images.githubusercontent.com/7872003/190384633-d1182e2d-5de4-4291-af0b-eb6e0965f421.gif)

Just get the content of the zip file ( [Warnings.pushbutton.zip](https://github.com/jmcouffin/rene_warnings/blob/a1aaab0e77c162e51fe9da230cd183170dc3b4bc/Warnings.pushbutton.zip) )in a folder like this one in your pyrevit install (implies you have pyRevit):

%AppData%\Roaming\pyRevit-Master\extensions\pyRevitTools.extension\http://pyRevit.tab\Project.panel\ptools.stack\Family.pulldown

you might have to remove the bundle.yaml of the higher level folder you see in this picture for it to show up
![Where to put it](https://user-images.githubusercontent.com/7872003/190349396-c191ae47-8a67-470c-9922-6e3605a64923.png)


after that, use the reload button in pyRevit and you should find the tool under pyRevit, Project, Family pulldown


Note: notice the pin icon at the top of the window to always keep it on top while managing the warnings

![image](https://user-images.githubusercontent.com/7872003/190386440-3289a5b4-412c-4013-bc46-c5a5d2a1ecd8.png)
If you like what I do, you can support me [@buymeacoffee](buymeacoffee.com/jmco)
