
//查看
function GoodsById2(storeId){
    url = "/app/gotoGoods_normal/goto/" + storeId;
    window.location = url;
}


//查找货物模态框函数
function Goodsinquiry2(){
    /*建立模态框对象*/
    modalBox = {};
    /*获取模var态框*/
    modalBox.modal = document.getElementById("inquiryModalGoods2");
    /*获得货物查询按钮*/
    modalBox.triggerBtn = document.getElementById("findGoods2");
    /*获得货物界面的关闭按钮*/
    modalBox.closeBtn = document.getElementById("inquirycloseBtnGoods2");
    
    /*模态框显示*/
    modalBox.show = function() {
        console.log(this.modal);
        this.modal.style.display = "block";
    }
    /*模态框关闭*/
    modalBox.close = function() {
        this.modal.style.display = "none";
    }
    /*当用户点击模态框内容之外的区域，模态框也会关闭*/
    modalBox.outsideClick = function() {
        var modal = this.modal;
        window.onclick = function(event) {
            if(event.target == modal) {
                modal.style.display = "none";
            }
        }
    }
    /*模态框初始化*/
    modalBox.init = function() {
        var that = this;
        this.triggerBtn.onclick = function() {
            that.show();
        }
        this.closeBtn.onclick = function() {
            that.close();
        }
        this.outsideClick();
    }
    modalBox.init();
}




