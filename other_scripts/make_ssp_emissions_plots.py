import sys, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rcParams['font.size'] = 5
plt.rcParams['figure.dpi'] = 300
size=5

sys.path.append("/div/no-backup/users/ragnhibs/simpleH2/hydrogen-simple-scenarios/src/")

from hydrogen_simple_scenarios import scenario_info, ssp_data_extraction



datapath_simpleh2 = "/div/no-backup/users/ragnhibs/simpleH2/simpleH2/input/"

def make_nox_co_ratio_and_ch4_plot(scenarios, title= "methane_and_nox_co_scenarios.png", include_nmvoc=True, other_colours=None, ratio_nox_co = True, add_time_points = None):
    ncols = 2
    if include_nmvoc:
        ncols = 3 #ncols+1
    if not ratio_nox_co:
        ncols = 3 # ncols+1
    fig, axs = plt.subplots(nrows=1,ncols=ncols,squeeze=True,figsize=(5*ncols*0.5,5*0.5),sharey=False)
    for scen, colour in scenario_info.scens_colours.items():
        if other_colours and scen in other_colours:
            colour = other_colours[scen]
        if scen not in scenarios:
            continue
        scenlabel = scen.upper()# scenario_info.scens_reverse[scen]
        data_co = pd.read_csv(os.path.join(datapath_simpleh2, f"co_emis_noburn_{scen}.csv"))
        data_nox = pd.read_csv(os.path.join(datapath_simpleh2, f"nox_emis_noburn_{scen}.csv"))
        data_ch4 = pd.read_csv(os.path.join(datapath_simpleh2, f"ch4_conc_{scen}.csv"))
        
        
        if ratio_nox_co:
            axs[0].plot(data_ch4["Years"].to_numpy(), data_ch4["Emis"].to_numpy(), color=colour, label = scenlabel)
            axs[1].plot(data_co["Years"].to_numpy(), data_nox["Emis"].to_numpy()/data_co["Emis"].to_numpy(), color=colour, label = scenlabel)
        else: 
            axs[0].plot(data_co["Years"].to_numpy(), data_nox["Emis"].to_numpy(), color=colour, label = scenlabel)
            axs[1].plot(data_co["Years"].to_numpy(), data_co["Emis"].to_numpy(), color=colour, label = scenlabel)
        if include_nmvoc:
            data_nmvoc = pd.read_csv(os.path.join(datapath_simpleh2, f"voc_emis_noburn_{scen}.csv"))
            axs[2].plot(data_nmvoc["Years"].to_numpy(), data_nmvoc["Emis"].to_numpy(), color=colour, label = scenlabel)
    
    for i,ax in enumerate(axs):
        ax.set_xlabel('Years')
        ax.set_xlim(left=1970, right=2060)
        #ax.set_ylim(bottom=0)
        ax.legend(fontsize=size,frameon=False)
        #ax.xaxis.set_major_locator(loc)
        axs[i].set_title(f"{chr(i+97)})", loc='left')
    
    if ratio_nox_co:
        axs[0].set_ylabel("Methane concentration [ppb]")
        axs[1].set_ylabel("NOx/CO emissions ratio")
    else: 
        axs[0].set_ylabel("NOx emissions [Tg NOx/yr]")
        axs[1].set_ylabel("CO emissions [Tg CO/yr]")
        #axs[0].set_title('Methane concentration', fontweight="bold")
        #axs[1].set_title('NOx/CO emissions', fontweight="bold")
        #if include_nmvoc:
        #axs[2].set_title('NMVOC emissions', fontweight="bold")
        axs[2].set_ylabel("NMVOC emissions [Tg NMVOC/yr]")

    if add_time_points:
        for ax in axs:
            for time_point in add_time_points:
                ax.axvspan(time_point-0.5, time_point+0.5, facecolor = "grey",edgecolor=None, alpha=0.5)
    plt.tight_layout()
    plt.savefig('Fig/'+title)

#data_path_iam = "/mnt/c/Users/masan/Downloads/Input_for_scenarios/SSP_IAM_V2_201811.csv"



#Figure 2for Ragnhild's paper
scenarios = ['ssp119', 'ssp434', 'ssp585']
make_nox_co_ratio_and_ch4_plot(scenarios, title= "methane_nox_co_ratio_for_ragnhild_fig2.png", include_nmvoc=False, other_colours={"ssp434": scenario_info.scens_colours["ssp126"]}, add_time_points=[2010,2050])

# Last supplementary figure for Ragnhild's paper
make_nox_co_ratio_and_ch4_plot(scenarios, title= "methane_nox_co_for_ragnhild_wnmvoc.png", include_nmvoc=True, ratio_nox_co = False, other_colours={"ssp434": scenario_info.scens_colours["ssp126"]}, add_time_points=[2010,2050])


