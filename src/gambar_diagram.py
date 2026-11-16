import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
fig, ax = plt.subplots(figsize=(8, 4.2))
ax.add_patch(Rectangle((2.5, 0.8), 4, 2.6, fc='#dbeafe', ec='black', lw=2))
ax.text(4.5, 2.2, r'Ruang Kelas' '\n' r'$V$ = 168 m$^3$' '\n' r'konsentrasi $C(t)$', ha='center', va='center', fontsize=12)
ax.add_patch(Rectangle((3.6, 0.8), 0.7, 0.35, fc='white', ec='black'))  # pintu
ax.add_patch(Rectangle((6.4, 1.9), 0.1, 0.9, fc='#fde68a', ec='black'))  # jendela
def arr(x1,y1,x2,y2,c='black'):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=18,lw=2,color=c))
arr(4.5,4.5,4.5,3.45,'#b91c1c'); ax.text(4.65,4.1,r'$G=n\,g$ (CO$_2$ dari 31 orang)',color='#b91c1c',fontsize=10)
arr(0.3,2.2,2.45,2.2,'#15803d'); ax.text(0.2,2.45,r'udara luar $C_{out}$=420 ppm',color='#15803d',fontsize=10)
arr(6.55,2.2,8.6,2.2,'#1d4ed8'); ax.text(6.7,2.45,r'udara keluar $Q\,C$',color='#1d4ed8',fontsize=10)
ax.text(4.5,0.3,r'Ventilasi $Q = Q_0 + c_v\,u_v$ (infiltrasi + bukaan jendela/pintu)',ha='center',fontsize=10)
ax.add_patch(plt.Circle((5.8,3.7),0.28,fc='#f59e0b',ec='black')); ax.text(5.8,3.7,'S',ha='center',va='center',fontsize=11,weight='bold')
ax.text(6.2,3.9,'Sensor CO$_2$',fontsize=10)
ax.set_xlim(0,9); ax.set_ylim(0,5); ax.axis('off')
plt.savefig('../figures/gambar_00_diagram.png', dpi=170, bbox_inches='tight'); 
