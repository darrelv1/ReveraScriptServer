

import React from "react"


const Navigation = (props) => {



    return (
      
<div classname="wrapper">
    <div className="header">
        <div className="header-info-box">
            <button className="menu-icon" id="menu-icon" type="button" data-toggle="my-info" />
            <span>Josh Sullivan</span>
        </div>
    </div>
    <nav className="nav">
        <a href="index.html"><span>←</span> Back</a>
    </nav>
    <article className="portfolio-projects">
        <div className="inner-wrapper flex-row-wrap two-col">
            <div className="project-info-box box">
            <h1>Project Name</h1>
            <p> 
                Available Tools to aid reporting and monthly acitivites. Monthly Reporting cleans the data from Journal Lines report and produces filter data that correspond to disposals, additions and transfers.
                Project Status, creates xlsx files and Asset info is a table of all the assets.
            </p>
            </div>
            <div className="project-tech-links-box box">
            <h6>Technologies</h6>
            <ul>
                <li>HTML</li>
                <li>CSS</li>
                <li>JavaScript</li>
                
            </ul>
            <a className="btn-link" href>Live Demo</a>
            <a className="btn-link" href>GitHub Repo</a>
            </div>
        </div>
        <div className="project-img-box box">
            <div className="Main-Report-links">
            <img className="img-Report-Link"  src="https://placehold.it/1200x550" alt="Screen capture of project"  />
            <span>Monthly Reporting</span>
        
            <img className="img-Report-Link"  src="https://placehold.it/1200x550" alt="Screen capture of project"  />
            <span>Project Status</span>
        
            <img className="img-Report-Link" src="https://placehold.it/1200x550" alt="Screen capture of project"/>
            <span>Asset Data</span>
            
            </div>
        </div>
        <nav className="nav">
            <a href="index.html"><span>←</span> Back</a>
        </nav>
    </article>
</div>
         
    )

}



export default Navigation 


