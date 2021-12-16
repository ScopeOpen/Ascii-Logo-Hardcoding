# Ascii-Logo-Hardcoding
Stop Hardcoding Ascii Logo's

# How to install colorama using pip
**[colorama Using Pip](https://pypi.org/project/colorama/)**

# Where to generate Ascii
**[Text to ASCII](http://www.patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=HI)**

# Hardcoded Ascii
```
Text = f"""
        
{color2}██{color1}╗ {color2} ██{color1}╗{color2}██{color1}╗
{color2}██{color1}║  {color2}██{color1}║{color2}██{color1}║
{color2}███████{color1}║{color2}██{color1}║
{color2}██{color1}╔══{color2}██{color1}║{color2}██{color1}║
{color2}██{color1}║  {color2}██{color1}║{color2}██{color1}║
{color1}╚═╝  ╚═╝╚═╝                                                                           

{Fore.RESET}"""
```
Effective but it takes way too long and if you want to be an efficent coder there's a way better way! **Refer to source code for full example**

# Simple Ascii

```
FirstText = f"""
        
██╗  ██╗██╗
██║  ██║██║
███████║██║
██╔══██║██║
██║  ██║██║
╚═╝  ╚═╝╚═╝                                                                           

{Fore.RESET}"""

Step1 = FirstText.replace("╝", f"{color2}╝")
Step2 = Step1.replace("═", f"{color2}═")
Step3 = Step2.replace("╚", f"{color2}╚")
Step4 = Step3.replace("╗", f"{color2}╗")
Step5 = Step4.replace("║", f"{color2}║")
Step6 = Step5.replace("╔", f"{color2}╔")
LastOutput = Step6.replace("█", f"{color1}█")
```
Much faster as you can easily change the definition of `color1` or `color2` to get a different output!  **Refer to source code for full example**

# Output of both
```
██╗  ██╗██╗
██║  ██║██║
███████║██║
██╔══██║██║
██║  ██║██║
╚═╝  ╚═╝╚═╝ 
``` 
(But with actual color)

# Enjoy Coding!
