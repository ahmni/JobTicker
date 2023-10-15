import React, { useState, useEffect } from 'react';
import { companyData } from '../App.js'


function CompanyListItem({ name, role, link, roleLink}: companyData ): JSX.Element {
  return (
    <tr>
      <td><a href={link}> {name} </a></td>
      <td><a href={roleLink}>{role} </a></td>
    </tr>
  );
}

export default CompanyListItem;
