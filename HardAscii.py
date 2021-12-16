from colorama import Fore, Style

b = Style.BRIGHT # ACTUAL STYLE OF COLORAMA!! CAN BE ANY STYLE

color1 = b+Fore.RED   # OUTLINE!! CAN BE ANY COLOR
color2 = b+Fore.WHITE # INSIDE!! CAN BE ANY COLOR

Text = f"""
        
{color2}██{color1}╗ {color2} ██{color1}╗{color2}██{color1}╗
{color2}██{color1}║  {color2}██{color1}║{color2}██{color1}║
{color2}███████{color1}║{color2}██{color1}║
{color2}██{color1}╔══{color2}██{color1}║{color2}██{color1}║
{color2}██{color1}║  {color2}██{color1}║{color2}██{color1}║
{color1}╚═╝  ╚═╝╚═╝                                                                           

{Fore.RESET}"""

print(Text)