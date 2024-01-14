import { companyData } from '../App.js'

export interface CompanyListItemProps {
  companyData: companyData;
  id: number;
}

function CompanyListItem(props: CompanyListItemProps): JSX.Element {
  return (
    <tr id={props.id.toString()}>
      <td><a href={props.companyData.link}> {props.companyData.name} </a></td>
      <td><a href={props.companyData.roleLink}>{props.companyData.role} </a></td>
    </tr>
  );
}

export default CompanyListItem;
