contractGeo = {}
contractGeo['AESAN'] = ['Brunei Darussalam', 'Cambodia', 'Indonesia',
                        "Laos People's Democratic Republic", 'Myanmar', 'Malaysia', 'Philippines', 'Singapore',
                        'Thailand', 'TimorLeste', 'Vietnam']
contractGeo['Australia/New Zealand'] = ['Australia', 'Christmas Island', 'Cocos(Keeling) Island', 'Cook Islands',
                                        'Fiji', 'Heard Island and Mcdonald Islands', 'Kiribati', 'Nauru',
                                        'New Zealand',
                                        'Niue', 'Norfolk Island', 'Papua New Guinea', 'Samoa', 'Solomon Islands',
                                        'Tokelau', 'Tonga', 'Tuvalu']
contractGeo['BeNeLux'] = ['Belgium', 'Luxembourg', 'Netherlands']
contractGeo['Brazil'] = ['Brazil']
contractGeo['Canada'] = ['Anguilla', 'Antigua and barbuda', 'Aruba', 'Bahamas', 'Barbados', 'Bermuda', 'Canada',
                         'Cayman Islands', 'Curacao', 'Dominica', 'Grenada', 'Guyana', 'Jamaica', 'Montserrat',
                         'Netherlands Antilles', 'Saint Kitts and Nevis', 'Saint Lucia',
                         'Saint Vincent and the Grenadines', 'Suriname', 'Trinidad and Tobago',
                         'Turks and Caicos Islands', 'Virgin Islands, British']
contractGeo['CEE'] = ['Albania', 'Armenia', 'Azerbaijan', 'Belarus', 'Bosnia and Herzegovina', 'Bulgaria',
                      'Croatia',
                      'Czech Republic', 'Estonia', 'Georgia', 'Hungary', 'Kazakhstan', 'Latvia', 'Lithuania',
                      'Macedonia, The former Yugoslav Republic of', 'Moldova, Republic of', 'Montenegro', 'Poland',
                      'Romania', 'Russian Federation', 'Serbia', 'Slovakia', 'Slovenia', 'Tajikistan',
                      'Turkmenistan',
                      'Ukraine', 'Uzbekistan']
contractGeo['DACH'] = ['Austria', 'Germany', 'Liechtenstein', 'Switzerland']
contractGeo['France'] = ['Andorra', 'Comoros', 'France', 'French Guiana', 'French Polynesia',
                         'French Southern Territories', 'Guadeloupe', 'Martinique', 'Mayotte', 'Monaco',
                         'New Caledonia', 'Reunion', 'Saint Pierre & Miquelon', 'Vanuatu', 'Wallis and Futuna']
contractGeo['Greater China'] = ['China', 'Hong Kong', 'Macao', 'Mongolia', 'Taiwan']
contractGeo['India South Asia'] = ['Bangladesh', 'Bhutan', 'India', 'Maldives', 'Nepal', 'Sri Lanka']
contractGeo['Italy'] = ['Holy See (Vatican City State)', 'Italy', 'San Marino']
contractGeo['Japan'] = ['Japan']
contractGeo['Korea'] = ['Korea, Republic of']
contractGeo['MEA'] = ['Afghanistan', 'Algeria', 'Angola', 'Bahrain', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi',
                      'Cameroon', 'Cape Verde', 'Central African Republic', 'Chad', 'Congo',
                      'Congo, The Democratic Republic of the', "Cote d'lvoire", 'Djibouti', 'Egypt',
                      'Equatorial Guinea', 'Eritrea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea',
                      'GuineaBissau',
                      'Iraq', 'Jordan', 'Kenya', 'Kuwait', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Madagascar',
                      'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger',
                      'Nigeria', 'Oman', 'Pakistan', 'Qatar', 'Rwanda', 'Sao Tome and Principe', 'Saudi Arabia',
                      'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan',
                      'Swaziland',
                      'Tanzania, United Republic of', 'Togo', 'Tunisia', 'Turkey', 'Uganda', 'United Arab Emirates',
                      'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']
contractGeo['Mexico'] = ['Mexico']
contractGeo['Nordic'] = ['Aland Islands', 'Bouvet Island', 'Denmark', 'Faroe Islands', 'Finland', 'Greenland',
                         'Iceland', 'Norway', 'Svalbard and Jan Mayen', 'Sweden']
contractGeo['SPGI'] = ['Cyprus', 'Greece', 'Israel', 'Malta', 'Portugal', 'Spain']
contractGeo['SSA'] = ['Argentina', 'Belize', 'Bolivia', 'Chile', 'Colombia', 'Costa Rica', 'Dominican Republic',
                      'Ecuador', 'El Salvador', 'Guatemala', 'Haiti', 'Honduras', 'Nicaragua', 'Panama', 'Paraguay',
                      'Peru', 'Uruguay', 'Venezuela']
contractGeo['UKI'] = ['British Indian Ocean Territory', 'Falkland Islands (Malvinas)', 'Gibraltar', 'Guernsey',
                      'Ireland', 'Isle of Man', 'Jersey', 'Pitcairn', 'Saint Helena',
                      'South Georgia and the South Sandwich Islands', 'United Kingdom']
contractGeo['United States'] = ['American Samoa', 'Guam', 'Marshall Islands', 'Micronesia, Federated States of',
                                'Northern Mariana Islands', 'Palau', 'Puerto Rico', 'United States',
                                'Virgin Islands, U.S.']


def getGeo(cntry):
    for j in list(contractGeo.keys()):
        if cntry in contractGeo[j]:
            return j