import { companyData } from '../App.js'
import CompanyListItem from './companyItem';
export interface CompanyListProps {
  companyDataList: companyData[];
}

function CompanyList({ companyDataList }: CompanyListProps): JSX.Element {
  const renderedCompanyItems: JSX.Element[] = companyDataList.map((companyData, index) => {
    return <CompanyListItem companyData={companyData} id={index}/>
  })
  return (
    <table>
      <thead>
        <tr>
          <th>Company</th>
          <th>Role</th>
        </tr>
      </thead>
      <tbody>
        {renderedCompanyItems ? renderedCompanyItems : undefined }
      </tbody>
    </table>
  );
}

export default CompanyList;
