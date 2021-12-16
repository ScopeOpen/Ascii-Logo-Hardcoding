from colorama import Fore, Style

b = Style.BRIGHT # ACTUAL STYLE OF COLORAMA!! CAN BE ANY STYLE

color1 = b+Fore.RED   # OUTLINE!! CAN BE ANY COLOR
color2 = b+Fore.WHITE # INSIDE!! CAN BE ANY COLOR

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

print(LastOutput)

# OUTPUT WILL BE COLORED TO WHATEVER YOU PICK!