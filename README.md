rogue-ips-api-csf
=================

Python source code. This plugs in a free Rogue IPs API service to CSF on your server. 

It will fetch the rogue IP addresses from the Secpanel network and add it to your CSF  block list.

It fetches the following information from your server:
<br>
 

<ul>
  <li> System Information (OS, Distribution, RAM & CPU) </li>
  <li> Banned IP Addresses</li>
</ul>

The API server maintains a Reputation Score for each server connected to it. If you  modify the script such that the information sharing from your server is stopped then the API server will change your server's Reputation Score and the service will stop for your server.

The service will be resumed when sharing of information is resumed from your server.

Installation
============

Please follow the following steps for installating this service:

<ol>
	<li>
		Download the scripts. These are also available at https://apis.secpanel.com/csf/downloads/csf-0.1.1.tar
<br>		A wget can be done as:

		<pre>
			wget https://apis.secpanel.com/csf/downloads/csf-0.1.1.tar
		</pre>
        </li>
	<li>
		Make run.py an executable by a simple chmod:
		<pre>
			chmod +x run.py
		</pre>
	</li>
	<li>
		Make it a daily cron job:
		<pre>
			cp run.py /etc/cron.daily/
			cp functions.py /etc/cron.daily/ 
		</pre>
		Note: Please do not increase the frequency of the cron job - not more than once every 24 hours. Fetching data at a higher than 24 hourly frequency will decrease your server's Reputation Score. 
	</li>
</ol>

*Please refer to Legal & Terms of Use @ https://apis.secpanel.com/legal.php  
