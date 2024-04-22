#!/bin/bash

URL="http://localhost:8081/ocs/v1.php/cloud/users"
USERNAME="admin"
PASSWORD="admin"
PASSWORD_ENCODED="abc123abc!" 


for i in {1..50}; do
    USERID="user$i"
    docker exec -i -u 33 cloud_base_app_1 bash -c "export OC_PASS=$PASSWORD && /var/www/html/occ user:add $USERID --password-from-env"
done

