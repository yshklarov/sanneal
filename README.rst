sanneal
=======

An implementation of the `simulated annealing <http://en.wikipedia.org/wiki/Simulated_annealing>`_
optimization algorithm.

Installation
------------

To run demos without installing::

    $ cd sanneal
    $ python3 -m sanneal.sanneal_demo

To install::

    $ cd sanneal
    $ easy_install .

Demos
-----

Random pixels:

.. image:: images/original.png

After "annealing":

.. image:: images/final.png

Traveling salesman problem -- fastest path to visit the capitals of all countries::

    Itinerary: Canada, United States of America, Bahamas, Jamaica,
    Haiti, Dominican Republic, Saint Kitts and Nevis, Antigua &
    Barbuda, Saint Lucia, Barbados, Dominica, Saint Vincent and the
    Grenadines, Grenada, Trinidad and Tobago, Venezuela, Colombia,
    Panama, Cuba, Belize, Mexico, Guatemala, El Salvador, Honduras,
    Nicaragua, Costa Rica, Ecuador, Peru, Bolivia, Chile, Argentina,
    Uruguay, Paraguay, Brazil, Guyana, Surinam, Cape Verde,
    Mauritania, Senegal, Gambia, Guinea-Bissau, Guinea, Sierra Leone,
    Liberia, Cote D'Ivoire, Ghana, Togo, Benin, Nigeria, Niger,
    Burkina Faso, Mali, Morocco, Portugal, Spain, Andorra, Monaco,
    Switzerland, Liechtenstein, Luxembourg, Netherlands, Belgium,
    France, United Kingdom, Ireland, Iceland, Norway, Sweden, Denmark,
    Germany, Czechoslovakia, Czech Republic, Austria, Slovakia,
    Hungary, Croatia, Slovenia, San Marino, Italy, Algeria, Tunisia,
    Libya, Malta, Greece, Albania, Montenegro, Bosnia-Herzegovina,
    Yugoslavia, Serbia, Macedonia, Bulgaria, Rumania, Moldova,
    Ukraine, Belarus, Lithuania, Poland, Latvia, Estonia, Finland,
    Russia, Azerbaijan, Iran, Turkmenistan, Tajikistan, Uzbekistan,
    Kyrgyz Republic, Kazakhstan, Pakistan, Afghanistan, Oman, United
    Arab Emirates, Bahrain, Qatar, Saudi Arabia, Kuwait, Iraq,
    Georgia, Armenia, Turkey, Cyprus, Lebanon, Syria, Jordan, Israel,
    Egypt, Sudan, Eritrea, Yemen, Yemen, People's Republic of,
    Djibouti, Ethiopia, Somalia, Tanzania, Zanzibar, Kenya, Uganda,
    Rwanda, Burundi, Central African Republic, Chad, Cameroon,
    Equatorial Guinea, São Tomé and Principe, Gabon, Congo, Democratic
    Republic of Congo, Angola, Namibia, Lesotho, Mozambique,
    Swaziland, South Africa, Botswana, Zimbabwe, Zambia, Malawi,
    Comoros, Madagascar, Mauritius, Seychelles, Maldives, Sri Lanka,
    Malaysia, Singapore, Indonesia, East Timor, Brunei, Vietnam,
    Cambodia, Thailand, Laos, Myanmar, Bangladesh, India, Nepal,
    Bhutan, Tibet, Mongolia, China, Korea, Japan, Taiwan, Philippines,
    Palau, Papua New Guinea, Solomon Islands, Federated States of
    Micronesia, Marshall Islands, Vanuatu, Samoa, Fiji, New Zealand,
    Australia.

    Total distance: 140003 km.
