#!/bin/sh
expect -c ”
spawn scp OutImage.jpg neojapan@serverhirosi.mydns.jp:public/rails/plant_monitor/public/image
expect {
  \”Are you sure you want to continue connecting (yes/no)?\” {
    send \”yes\r\”
    expect \”password:\”
    send \”（len7se4545）\r\”
  } \”password:\” {
    send \”（len7se4545）\r\”
  }
}
interact
"
