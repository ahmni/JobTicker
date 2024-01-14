import React, { useEffect } from 'react';
import './App.css';
import CompanyList from './components/companyList';

export interface companyData {
  name: string;
  link: string;
  role: string;
  roleLink: string;
}

const BACKEND_URL = 'http://localhost:5050/';


function App() {
  const [companyData, setCompanyData] = React.useState<companyData[]>([]);
  useEffect(() => {
    setTimeout(() => {
      fetch(BACKEND_URL)
        .then(response => response.json())
        .then(json => {
          if (json !== undefined){
            setCompanyData(json.body);
          }
        })
        .catch(error => console.error(error));
    }, 1000);
  }, []);
  console.log(companyData)
  return (
    <div className="App">
      <header className="App-header">
        <div>
          {companyData.length > 0 ? <CompanyList companyDataList={companyData}/> : 'Loading...'}
        </div>
      </header>
    </div>
  );
}

export default App;
