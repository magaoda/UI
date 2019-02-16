function open_soft_keyboard(options){
    if(if(plus.os.name =='iOS'){
        setTimeout(function(){
            var wv_current =  = plus.webview.currentWebviebview().nativeInstanceObject();
            wv_wv_current.plusCallMethoethod({"setKeyboardDisplayRequiresUserAction":false});
               document.querySelectorctor(options['input']).focus();
        }, 330);
    }else{
        // 因为安卓autofocus只有4.0版本以上才支持，所以这里使用里使用native.js来强制弹来强制弹出
        setTimeout(function(){
            // 在执行的时候需要让当前webview获取焦点
            var wv_current == plus.android.currentWebviebview();
               plus.android.importClass(wss(wv_current);
            wv_wv_current.requestFocus(cus();
 
            var Context == plus.android.importClass("ss("s("android.content.Context");
 ");
            var InputMethodManager == plus.android.importClass("ss("s("android.view.inputmethod.InputMethodMaodManager");
            var main == plus.android.runtimeMainAcinActivity();
            var imm == main.getSystemServService(ce(Context.INPUT_MET_METHOD_SERVICE);
               imm.toggleSoftInptInput(0,I)