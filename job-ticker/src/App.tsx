import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import CompanyList from './components/companyList';

export interface companyData {
  name: string;
  link: string;
  role: string;
  roleLink: string;
}




function App() {
  const [companyData, setCompanyData] = React.useState<companyData[]>([{
    name: '',
    link: '',
    role: '',
    roleLink: '',
  }]);
  useEffect(() => {
    fetch('http://localhost:5050/')
    .then(response => response.json())
    .then(json => {
      if (json !== undefined){
        setCompanyData(json.body);
      }
    })
    .catch(error => console.error(error));
  }, []);
  console.log(companyData)
          //{companyData ? <CompanyList {...companyData}/> : 'Loading...'}
  return (
    <div className="App">
      <header className="App-header">
        <div>
          {companyData ? <CompanyList companyDataList={companyData}/> : 'Loading...'}
        </div>
      </header>
    </div>
  );
}

export default App;
