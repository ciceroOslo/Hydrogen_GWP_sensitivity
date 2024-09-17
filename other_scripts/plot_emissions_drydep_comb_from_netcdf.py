import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import sys
import datetime 

sys.path.append('/div/qbo/users/ragnhibs/Python/')
print(sys.path)

#import area_calcs_irregular

plt.rcParams['font.size'] = 5
plt.rcParams['figure.dpi'] = 300

plot_name = True

noOfCols=1
noOfRows=2 
fig, axes = plt.subplots(nrows=noOfRows,ncols=noOfCols, figsize=(8/2,6/2), subplot_kw=dict(projection=ccrs.PlateCarree()))



cmap = plt.get_cmap('YlOrBr')
levels = [0,0.1,0.5,1,5,10,50,100,500,1000,1500]

ax = axes[0]
print(levels)

ax.coastlines(linewidth=0.75)
ax.set_global()

data_emis_annual = xr.open_dataset('fig1a.nc')
data_emis_annual['antro_ship'].plot(ax=ax,cmap=cmap,levels=levels,cbar_kwargs={'ticks': levels,'label':None,'format':'%4.1f'})

ax.set_title('a) Annual Anthropogenic H$_2$ emissions [mg m$^{-2}$ yr$^{-1}$]',loc='left')

points = {"nemo":[-48.52, -123.23],
          "epia":[46.17, 85.58],
          "munich":[48.137, 11.576124],
          "maxdep":[3.365,41.06],
          "usdrydep":[34.77,-100.7],
          "zep": [78.5, 11.56],
          "maud":[-72.3, 12]}
for x in points:
    print(points[x])
    lon = points[x][1]
    lat = points[x][0]
    print(lon)
    print(lat)

    ax.plot(lon,lat, '*',color='darkblue',markersize=3,transform=ccrs.PlateCarree())







data_drydep = xr.open_dataset('fig1b.nc')



cmap = plt.get_cmap('YlOrBr')
ax = axes[1]


levels = np.arange(0,1500,200)


ax.coastlines(linewidth=0.75)
ax.set_global()

data_drydep['h2drydep'].plot(ax=ax,cmap=cmap,levels=levels,cbar_kwargs={'ticks': levels,'label':None})


ax.set_title(None)
ax.set_title('b) Annual Soil Sink H$_2$ [mg m$^{-2}$ yr$^{-1}$]',loc='left')


for x in points:
    print(points[x])
    lon = points[x][1]
    lat = points[x][0]
    print(lon)
    print(lat)

    ax.plot(lon,lat, '*',color='darkblue',markersize=3,transform=ccrs.PlateCarree())
    if plot_name:
        ax.text(lon+5,lat,x,color='darkblue',horizontalalignment='left',
                verticalalignment='center')
    
plt.tight_layout()

plt.savefig('Fig/figure_1.png')
plt.show()

exit()
