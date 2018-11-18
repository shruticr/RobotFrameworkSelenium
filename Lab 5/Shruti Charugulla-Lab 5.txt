<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<meta content="text/html; charset=UTF-8" http-equiv="content-type" />
	<title>Lab 5-Shruti Charugulla</title>
</head>
<body>
<table cellpadding="1" cellspacing="1" border="1">
<thead>
<tr><td rowspan="1" colspan="3">Test Case 1</td></tr>
</thead>
<tbody>
<tr>
    <td>open</td>
    <td>http://www.austincc.edu/wtucker/
        <datalist>
            <option>http://www.austincc.edu/wtucker/</option>
        </datalist>
    </td>
    <td></td>
</tr>
<tr>
    <td>clickAt</td>
    <td>link=ITSE 1392 - Special Topics - Automated Software Testing
        <datalist>
            <option>link=ITSE 1392 - Special Topics - Automated Software Testing</option>
            <option>//a[contains(text(),'ITSE 1392 - Special Topics - Automated Software Testing')]</option>
            <option>//a[contains(@href, 'ITSE1392/fallautotesting.htm')]</option>
            <option>//a[2]</option>
        </datalist>
    </td>
    <td>57,13</td>
</tr>
<tr>
    <td>clickAt</td>
    <td>link=Synonym 34859
        <datalist>
            <option>link=Synonym 34859</option>
            <option>//a[contains(text(),'Synonym 34859')]</option>
            <option>//a[contains(@href, 'ITSE1392fall17.pdf')]</option>
            <option>//h4/a</option>
        </datalist>
    </td>
    <td>39,8</td>
</tr>
</tbody></table>
<table cellpadding="1" cellspacing="1" border="1">
<thead>
<tr><td rowspan="1" colspan="3">Test Case 2</td></tr>
</thead>
<tbody>
<tr>
    <td>open</td>
    <td>http://www.austincc.edu/wtucker/
        <datalist>
            <option>http://www.austincc.edu/wtucker/</option>
        </datalist>
    </td>
    <td></td>
</tr>
<tr>
    <td>clickAt</td>
    <td>link=ITSE 1391 - Special Topics - Fundamentals of Software Testing
        <datalist>
            <option>link=ITSE 1391 - Special Topics - Fundamentals of Software Testing</option>
            <option>//a[contains(text(),'ITSE 1391 - Special Topics - Fundamentals of Software Testing')]</option>
            <option>//a[contains(@href, 'ITSE1391/fallsoftwaretesting.htm')]</option>
            <option>//td/a</option>
        </datalist>
    </td>
    <td>90,8</td>
</tr>
<tr>
    <td>clickAt</td>
    <td>link=Synonym 34854
        <datalist>
            <option>link=Synonym 34854</option>
            <option>//a[contains(text(),'Synonym 34854')]</option>
            <option>//a[contains(@href, 'ITSE1391fall17.pdf')]</option>
            <option>//h4/a</option>
        </datalist>
    </td>
    <td>45,8</td>
</tr>
</tbody></table>
</body>
</html>