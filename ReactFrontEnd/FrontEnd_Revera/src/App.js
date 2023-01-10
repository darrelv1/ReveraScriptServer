import logo from './logo.svg';
import './App.css';
import Sidebar from './Components/Sidebar'
import React from 'react'
import Header from './Components/Header';
import Navigation from './Components/Home'

function App() {

  
  const tools = ["Monthly Reporting", "Project Status", "Asset Info"]

  return (
      <div>
        <Navigation props={["Monthly Reporting", "Project Status", "Asset Info"]} />
        <Sidebar props={["Monthly Reporting", "Project Status", "Asset Info"]}/>
      </div>

      


  );
}

export default App;
