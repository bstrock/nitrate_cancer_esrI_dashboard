<h1>ArcGIS Experience Builder App:  Wisconsin Nitrate-Cancer Dashboard</h1>

This web app was built as an example implementation of building an interactive data exploration tool in ArcGIS Online Experience Builder, using data processed and staged using the ArcGIS for Python API using a Jupyter Notebook.

The Jupyter environment was used to generate the spatial data and analysis layers, then publish them to AGOL, where additional tweaking and revisions took place.  Like many Jupyter notebooks, it was developed exactly enough to get to the next development phase, and thus hasn't been as organized or extensively documented.

Please note that this app was built for a class assignment for my MS in GIS and Cartography, and that the assignment required the use of simulated data provided by the lab materials.  As such, this app should not be considered authoritative.

<h2>Link to live project</h2>

[Wisconsin Nitrate-Cancer Dashboard](https://uw-mad.maps.arcgis.com/apps/webappviewer/index.html?id=7d7e739eff3d45d490ea207f4c7ee40f)

<h2>Project Materials</h2>

[Watch a short demo video here](https://youtu.be/3v9xWQ_Xax8)


<h2>App Features</h2>

- Visualize the location and sampled nitrate levels at wells sites all across Wisconsin
- Access beautiful interpolation surfaces designed to estimate nitrate levels at unsampled locations
- Visualize community cancer levels based on demographic data
- Use additional map analysis tools, such as Measure and Generate Hotspots
- Curated tooltips to provide additional datapoint insights
- Linked visualizations to summarize attribute distributions
- Integration between desktop data generation/processing, publication via ArcGIS Online, and interface design using ArcGIS Online-provided tools

<h2>Screenshots</h2>

<img src="https://github.com/bstrock/nitrate_cancer_dashboard/blob/master/dashboard-screenshot-1.png" width="25%"></img> 
<img src="https://github.com/bstrock/nitrate_cancer_dashboard/blob/master/dashboard-screenshot-2.png" width="25%"></img>
<img src="https://github.com/bstrock/nitrate_cancer_dashboard/blob/master/dashboard-screenshot-3.png" width="25%"></img>



<h2>Project Materials</h2>

[Watch a short project overview walkthrough](https://youtu.be/EvkzLfWa2Ko)

[Check out the backend FastAPI app repo](https://github.com/bstrock/playground_finder)

[Use the interactive API documentation](https://eden-prairie-playgrounds.herokuapp.com/docs#/)

<h2> Supporting Documents</h2>

[Project Proposal](https://github.com/bstrock/playground_planner/blob/master/data/docs/Brian%20Strock%20-%20Project%20Proposal.docx)

[Project Plan](https://github.com/bstrock/playground_planner/blob/master/data/docs/Brian%20Strock%20Project%20Plan.pdf)

[Project Executive Summary](https://github.com/bstrock/playground_planner/blob/master/data/docs/Brian%20Strock%20778%20Executive%20Summary.docx)


<h2>Tech Stack</h2>

* React.js
* Leaflet.js
* react-leaflet
* Material UI
* Geoapify
* Mapbox/ESRI (basemaps)

<h2>Project Structure and Contents</h2>

```
site/
├── public/
│       ├── CNAME
|       ├── favicon.ico
│       ├── index.html
│       ├── manifest.json
│       └── logo.txt
└── src/
        ├── /components
        |     ├── /FilterDrawer
        |     |      ├── AccordionTemplate.js
        |     |      ├── DistanceSlider.js
        |     |      ├── EquipmentCheckboxList.js
        |     |      ├── FilterAccordion.js
        |     |      ├── FilterDrawer.js
        |     |      ├── FloatingButton.js
        |     |      └── ParkButton.js
        |     ├── /Map
        |     |      ├── /LeafletLayers
        |     |      |     ├── LayerControl.js
        |     |      |     ├── LocationMaker.js
        |     |      |     ├── PlaygroundMarker.js
        |     |      |     └── UserGuide.js
        |     |      ├── /ParkPopup
        |     |      |     ├── AddressBlock.js
        |     |      |     ├── AssetTable.js
        |     |      |     ├── EquipmentCard.js
        |     |      |     ├── InfoBox.js
        |     |      |     ├── ParkCard.js
        |     |      |     └── ParkCardActionBar.js
        |     |      └── /StaticLayers
        |     |            ├── PlaygroundPolygons.js
        |     |            └── TileLayers.js
        |     ├── App.js
        |     ├── NavBar.js
        |     └── ApiQuery.js
        ├── /data
        |     └── ep_boundary.json
        ├── /images
        |     ├── /icons
        |     |     └── ...svg elements
        |     ├── /leaflet
        |     |     └── ...leaflet base icons
        |     ├── /playgrounds
        |     |     └── ...images of playgrounds
        |     └── hero.png
        ├── App.css
        ├── index.css
        ├── index.js
        └── reportWebVitals.js   
```

`/public` contains resources for site hosting and publication.

`/src` contains website source code, including all custom React components, images, data, and api loading.

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).


# nitrate_cancer_dashboard

Link to final project:  https://uw-mad.maps.arcgis.com/apps/webappviewer/index.html?id=7d7e739eff3d45d490ea207f4c7ee40f
