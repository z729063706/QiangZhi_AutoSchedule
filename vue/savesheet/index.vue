<template>
  <div class="app-container">
    <el-form
      label-width="100px"
      :inline="true"
      class="demo-form-inline"
    >

    <el-form-item label="学号:"> 
        <el-input  v-model="username" style="width: 150px" placeholder="教务处登录账号" />

      </el-form-item>



      <el-form-item label="密码：" label-width="100px">
        <el-input  type="password" v-model="password" style="width: 200px" placeholder="仅用作自动获取课表使用" />
      </el-form-item> 
      <br>
      <el-form-item label="备注:"> 
        <el-input  v-model="notice" style="width: 400px" placeholder="可备注是否新校区，排班喜好等" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary"  :disabled="btn"  @click="getSheets()" >点击提交</el-button>
      </el-form-item>    
    </el-form>
    <p style="font-size:16px" v-html="re"></p>
    <p style="font-size:16px" >如果课表获取成功，您将会看到上方返回信息</p>
    <p style="font-size:16px" >导播部课表收集系统，出现问题联系请19导播赵云浩</p>
   
   
  </div>
  
</template>


<style>
  .el-select__tags-text {
    display: inline-block;
    max-width: 120px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .el-select .el-tag__close.el-icon-close {
    top: -7px;
  }
  .el-table .cell {
  white-space: pre-line;
  }
</style>



<script>
import { getSheets } from "@/api/report";
import { Message } from 'element-ui'
export default {
    data() {
    return {
      username : '',
      password : '',
      notice : '',
      re : '请点击提交',
      btn : false
    }
},
    mounted() {    
        
},
    methods: {
        getSheets(){
          if (!this.username || !this.password){
            this.re = '请输入用户名及密码！'
            return
          }
            console.log(this.username,this.password);
            //return
            this.btn = true
            this.re = '请等待系统响应......'
            getSheets({
                username : this.username,
                password : this.password,
                notice : this.notice,
            }).then(response => {
            console.log('response',response);
            this.re = response.data
            this.btn = false
          })
        },
        
}
}
</script>