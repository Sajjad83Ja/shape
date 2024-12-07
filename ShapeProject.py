import matplotlib.pyplot as plt
import matplotlib.patches as ptch
import matplotlib.image as mpimg
import os

fig , ax = plt.subplots()

os.chdir(os.path.dirname(os.path.abspath(__file__)))
User = mpimg.imread('UserPic.jpg')

Xrr, Yrr, Wrr, Hrr = 5, 87, 110, 7.5
rounded_rect = ptch.FancyBboxPatch(
    (Xrr, Yrr),Wrr,Hrr,
    boxstyle="round,pad=3,rounding_size=6.5",
    ls = "--",edgecolor='black',facecolor='none')
ax.add_patch(rounded_rect)
ax.text(Xrr+Wrr-(12+8)+12,Yrr+2.5,"Users",fontsize=6)

for i in [Xrr+3.5, (Wrr/2)+Xrr-6-3.5, Xrr+Wrr-(12+8)]:
    ax.imshow(User, extent=(i, i+12, Yrr-1, Yrr+Hrr+1))
    plt.arrow(i+4, Yrr-3, 0, -4, head_width=3, head_length=1, fc='k', ec='k',lw=0.4)
    plt.arrow(i+8, Yrr-8, 0, 3.5, head_width=3, head_length=1, fc='k', ec='k',lw=0.4)

Hrr2 = 18
move= 0
for i in range(0,3):
    ax.add_patch(ptch.FancyBboxPatch((Xrr+move, Yrr-(Hrr/2)-Hrr2-8),Wrr/3 -7,Hrr2,boxstyle="round,pad=3,rounding_size=5",ls = "-",edgecolor='black',facecolor='none',lw=0.3))
    move+= Xrr+ Wrr/3 -1.5

ax.set_xlim(-23,200)
ax.set_ylim(-65,100)

ax.add_patch(ptch.Rectangle((3,63),4,10,facecolor="none",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((5,65.5),1.2,facecolor="red",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((5,70.5),1.2,facecolor="red",edgecolor="black",lw=0.4))
plt.arrow(7,68,3,5, head_width=1, head_length=1.8, fc='k', ec='k',lw=0.4)
plt.arrow(7,68,3,-5, head_width=1, head_length=1.8, fc='k', ec='k',lw=0.4)

ax.add_patch(ptch.Rectangle((11,68),4,10,facecolor="none",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((13,70),1.2,facecolor="yellow",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((13,73),1.2,facecolor="yellow",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((13,76),1.2,facecolor="yellow",edgecolor="black",lw=0.4))

ax.add_patch(ptch.Rectangle((11,56),4,10,facecolor="none",edgecolor="black",lw=0.4))
plt.arrow(15,73,4.7,0, head_width=1, head_length=1.3, fc='k', ec='k',lw=0.4)
plt.arrow(15,61,4.7,0, head_width=1, head_length=1.3, fc='k', ec='k',lw=0.4)
ax.add_patch(ptch.Circle((13,58),1.2,facecolor="cyan",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((13,61),1.2,facecolor="cyan",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((13,64),1.2,facecolor="cyan",edgecolor="black",lw=0.4))

ax.add_patch(ptch.Rectangle((21,68),4,10,facecolor="none",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((23,70.5),1.2,facecolor="#10c425",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((23,75.5),1.2,facecolor="#10c425",edgecolor="black",lw=0.4))

ax.add_patch(ptch.Rectangle((21,56),4,10,facecolor="none",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((23,58),1.2,facecolor="#d25e0a",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((23,61),1.2,facecolor="#d25e0a",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((23,64),1.2,facecolor="#d25e0a",edgecolor="black",lw=0.4))

plt.arrow(25,61,3.8,4.5, head_width=1, head_length=1.8, fc='k', ec='k',lw=0.4)
plt.arrow(25,73,3.8,-4.5, head_width=1, head_length=1.8, fc='k', ec='k',lw=0.4)

ax.add_patch(ptch.Rectangle((30,63),4,10,facecolor="none",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((32,65),1.2,facecolor="#4e0f75",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((32,68),1.2,facecolor="#4e0f75",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((32,71),1.2,facecolor="#4e0f75",edgecolor="black",lw=0.4))

ax.add_patch(ptch.Rectangle((45,63),4,10,facecolor="none",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((47,65.5),1.2,facecolor="red",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((47,70.5),1.2,facecolor="red",edgecolor="black",lw=0.4))
plt.arrow(49,68,6.5,5, head_width=1, head_length=1.8, fc='k', ec='k',lw=0.4)
plt.arrow(49,68,6.5,-5, head_width=1, head_length=1.8, fc='k', ec='k',lw=0.4)

ax.add_patch(ptch.Rectangle((57,68),4,10,facecolor="none",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((59,70),1.2,facecolor="yellow",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((59,73),1.2,facecolor="yellow",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((59,76),1.2,facecolor="yellow",edgecolor="black",lw=0.4))

ax.add_patch(ptch.Rectangle((57,56),4,10,facecolor="none",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((59,58),1.2,facecolor="cyan",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((59,61),1.2,facecolor="cyan",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((59,64),1.2,facecolor="cyan",edgecolor="black",lw=0.4))

plt.arrow(61,61,6.5,5, head_width=1, head_length=1.8, fc='k', ec='k',lw=0.4)
plt.arrow(61,73,6.5,-5, head_width=1, head_length=1.8, fc='k', ec='k',lw=0.4)

ax.add_patch(ptch.Rectangle((69,63),4,10,facecolor="none",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((71,65),1.2,facecolor="#4e0f75",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((71,68),1.2,facecolor="#4e0f75",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((71,71),1.2,facecolor="#4e0f75",edgecolor="black",lw=0.4))

ax.add_patch(ptch.Rectangle((85,63),4,10,facecolor="none",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((87,65.5),1.2,facecolor="red",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((87,70.5),1.2,facecolor="red",edgecolor="black",lw=0.4))

ax.add_patch(ptch.Rectangle((93,63),4,10,facecolor="none",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((95,65),1.2,facecolor="yellow",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((95,68),1.2,facecolor="yellow",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((95,71),1.2,facecolor="yellow",edgecolor="black",lw=0.4))

ax.add_patch(ptch.Rectangle((102,63),4,10,facecolor="none",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((104,65),1.2,facecolor="cyan",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((104,68),1.2,facecolor="cyan",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((104,71),1.2,facecolor="cyan",edgecolor="black",lw=0.4))

ax.add_patch(ptch.Rectangle((110,63),4,10,facecolor="none",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((112,65),1.2,facecolor="#4e0f75",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((112,68),1.2,facecolor="#4e0f75",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Circle((112,71),1.2,facecolor="#4e0f75",edgecolor="black",lw=0.4))

plt.arrow(89,68,2.7,0, head_width=1, head_length=1.3, fc='k', ec='k',lw=0.4)
plt.arrow(97,68,3.7,0, head_width=1, head_length=1.3, fc='k', ec='k',lw=0.4)
plt.arrow(106,68,2.7,0, head_width=1, head_length=1.3, fc='k', ec='k',lw=0.4)

ax.add_patch(ptch.FancyBboxPatch((0, -45),120,90,boxstyle="round,pad=3,rounding_size=6.5",ls = "--",edgecolor='black',facecolor='none'))
ax.add_patch(ptch.FancyBboxPatch((3, -42),80,84,boxstyle="round,pad=3,rounding_size=6.5",ls = "-",edgecolor='black',facecolor='none',lw=0.4))

ax.add_patch(ptch.Rectangle((4,-43),78,39,facecolor="none",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Rectangle((4,1),78,38,facecolor="none",edgecolor="black",lw=0.4))
plt.arrow(18,55,0,-13.5, head_width=1.6, head_length=2.5, fc='k', ec='k',lw=0.4)
plt.arrow(43,1,0,-2.5, head_width=3, head_length=2.5, fc='k', ec='k',lw=0.4)
plt.text(19,40.5,"Task Scheduler",fontsize=5.2)


xs = [7, 13,13, 37,37, 65]
ws = [6, 24,18, 24,28, 13]
color = ["red","yellow","cyan","green","orange", "#4e0f75"]
y=34

for p in range(0,2):
    for i in range(0,len(xs)):
        C = 0
        for t in range(0,2 if i==3 else 3):
            ax.add_patch(ptch.Rectangle((xs[i],y),ws[i],2,facecolor=f"{color[i]}",edgecolor="black",lw=0.4))
            C += (y+2)
            y -= 2
        if p==0 :
            C = y+4 if i==3 else ((C+y)/4)+0.4
            plt.plot([xs[i]+ws[i],82],[C,C],color='black',lw=0.4)
    y = -8

plt.arrow(7,-40,0,34.5, head_width=1.5, head_length=1.5, fc='k', ec='k',lw=0.4)
plt.arrow(7,-40,72.6,0, head_width=1.5, head_length=1.5, fc='k', ec='k',lw=0.4)

plt.text(18,35,"Order Relationship of Task Instances",fontsize=5)
plt.text(28,-9,"Task Scheduling",fontsize=6)
plt.text(9,-6,"Containers",fontsize=3.5)

ax.add_patch(ptch.FancyBboxPatch((97, -36),20,55,boxstyle="round,pad=3,rounding_size=7.5",ls = "-",edgecolor='black',facecolor='#D3D3D3',lw=0.4,alpha=0.5))

plt.arrow(82,-26,10.5,0, head_width=2, head_length=1.5, fc='k', ec='k',lw=0.4)
ax.add_patch(ptch.Rectangle((97,-33),20,12,facecolor="white",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Rectangle((97,-17),20,12,facecolor="white",edgecolor="black",lw=0.4))
ax.add_patch(ptch.Rectangle((97,-1),20,12,facecolor="white",edgecolor="black",lw=0.4))
ax.text(99,38,"MWMS",fontsize=8)
ax.text(97,15,"Controller",fontsize=7)
ax.text(98,1,"  Cloud\nManager",fontsize=7)
ax.text(98,-15,"Container\nAllocator",fontsize=6.5)
ax.text(99,-29,"Monitor",fontsize=7)

plt.arrow(120,5,6.5,0, head_width=2, head_length=2.5, fc='k', ec='k',lw=0.4)
plt.arrow(120,-11,6.5,0, head_width=2, head_length=2.5, fc='k', ec='k',lw=0.4)
plt.arrow(129,-27,-6.5,0, head_width=2, head_length=2.5, fc='k', ec='k',lw=0.4)

ax.text(133,93,"Hybrid Cloud",fontsize=5)
ax.add_patch(ptch.FancyBboxPatch((132, -45),60,139.5,boxstyle="round,pad=3,rounding_size=6.5",ls = "--",edgecolor='black',facecolor='none'))
ax.add_patch(ptch.FancyBboxPatch((135, 28),54,60,boxstyle="round,pad=3,rounding_size=6.5",ls = "-",edgecolor='black',facecolor='none',lw=0.4))
ax.add_patch(ptch.FancyBboxPatch((135, -42),54,54,boxstyle="round,pad=3,rounding_size=6.5",ls = "-",edgecolor='black',facecolor='none',lw=0.4))

Orange_D = mpimg.imread("OrangeDocker.jpg")
Violet_D = mpimg.imread("VioletDocker.jpg")
Blue_D = mpimg.imread("BlueDocker.jpg")
Yellow_D = mpimg.imread("YellowDocker.jpg")

for i in [[(135,-41),(177,-36),"VMb3",[Orange_D,(137,147.7,-40,-30),Violet_D,(148,158.7,-40,-30),None,None]],[(135,-24),(177,-19),"VMb2",[Orange_D,(137,147.7,-23,-13),Violet_D,(148,158.7,-23,-13),None,None]],[(135,-7),(177,-2),"VMb1",[Orange_D,(137,147.7,-6,4),Violet_D,(148,158.7,-6,4),None,None]],
           [(135,29),(177,34),"VMa3",[Yellow_D,(137,147.7,30,40),Blue_D,(148,158.7,30,40),None,None]],[(135,46),(177,51),"VMa2",[Orange_D,(137,147.7,47,57),Yellow_D,(148,158.7,47,57),Blue_D,(159,169.7,47,57)]],[(135,69),(177,74),"VMa1",[Orange_D,(137,147.7,70,80),Yellow_D,(148,158.7,70,80),Blue_D,(159,169.7,70,80)]]]:
    ax.add_patch(ptch.Rectangle(i[0],54,12,facecolor="#D3D3D3",edgecolor="black",lw=0.4,alpha=0.5))
    ax.text(i[1][0],i[1][1],i[2],fontsize=6)
    for p in range(0,6,2):
        if i[3][p] is not None :
            plt.imshow(i[3][p],extent=i[3][p+1],zorder=2)

ax.text(139,85,"Cloud a",fontsize=7)
ax.text(139,9,"Cloud b",fontsize=7)
ax.text(69,-43,"Time",fontsize=4.85)
ax.text(161,17,"Transmission time\nin different douds",fontsize=4.4)
ax.text(166,60,"Transmission time\n   in same douds",fontsize=4.4)

ax.add_patch(ptch.FancyBboxPatch((138.3, -38),6.25,40.6,boxstyle="round,pad=3,rounding_size=6.5",ls = "--",edgecolor='black',facecolor='none',lw=1,zorder=2.1))
ax.add_patch(ptch.FancyBboxPatch((139.1, 46),5.35,32.6,boxstyle="round,pad=3,rounding_size=6.5",ls = "--",edgecolor='black',facecolor='none',lw=1,zorder=2.1))

xL = [148.4, 148.4, 148.85, 149.61, 150.42, 151.33, 152.69, 154.05, 155.67, 156.53, 157.54, 158,   158.45, 158.62, 158.66, 158.5,  158.4, 158.4, 158.15, 157.75, 157.09, 143.73, 141.76, 140.23, 138.62, 137.9, 137.54, 137.61, 137.52, 137.61, 137.85, 138.09, 138.7, 147.64, 148.11, 148.49]
yL = [46,    78.5,  79.08,   80.14, 81.15,   81.86, 82.27,  82.27,  82.11,  81.46,  80.85,  80.35, 79.39,  78.68,  77.82,  76.96,  75.8,  50,    50.09,  48.57,  47.4,   31.35,  30.37,  30.1,   30.82,  32.25, 34.4,   33.04,  33.89,  34.65,  35.5,   36.21,  36.83, 44.25,  44.96,  45.77] 
plt.plot(xL,yL,ls="--",lw=1,color="black")

xL2= [ x+10.9 for x in xL ]
plt.plot(xL2,yL,ls="--",lw=1,color="black")

plt.plot([159,167,147.5],[67,63,60],ls="-",lw=0.3,color="black")
plt.plot([153,160],[30.5,20],ls="-",lw=0.3,color="black")
plt.arrow(160,20,-14,-15, head_width=1.2, head_length=0.5, fc='k', ec='k',lw=0.3,zorder=2.2)
plt.text(-20,-60,"Fig. 1.   Scheduling framework in cloud.",fontsize=11)

plt.show()