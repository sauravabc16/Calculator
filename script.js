var result = '';
function getValue(num){
    result+=num;
    document.getElementById("disp").value = result;    
}

function equal(){

    try{
        ans=eval(result);
    }
    catch(err){
        ans = "Error";
    }
    document.getElementById("history").innerText = result;
    document.getElementById("disp").value = ans;
    result = ans;
    console.log(result, ans);
}

function clr(){
    if(result==''){
        document.getElementById("history").innerText = result;
    }
    else{
        result='';
        document.getElementById("disp").value = result;
    }
}

function backspace(){
    if(result=="Error")
        return;
    result = result.substring(0,result.length-1);
    document.getElementById("disp").value = result;
}