<template>
<div class="app-container">
    <el-form
      label-width="100px"
      :inline="true"
      class="demo-form-inline"
    >
<el-form-item label="周次：">
  <el-select v-model="weekSearch"  placeholder="请选择周次">
    <el-option
      v-for="item in weeks"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
</el-form-item>

<el-form-item label="日期：">
  <el-select v-model="daySearch"  placeholder="请选择日期">
    <el-option
      v-for="item in days"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
</el-form-item>

<el-form-item label="周次：">
  <el-select v-model="lessonSearch"  placeholder="请选择课节">
    <el-option
      v-for="item in lessons"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
</el-form-item>

<el-form-item>
        <el-button type="primary"  @click="freeSearch()" >点击搜索</el-button>
</el-form-item>  
</el-form>

<el-table
      v-loading="listLoading"
      :data="res"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
    >   
    <el-table-column label="姓名" width="100" align="center">
        <template slot-scope="scope">
          {{ scope.row[0] }}
        </template>
      </el-table-column>
    <el-table-column label="学号" width="100" align="center">
        <template slot-scope="scope">
          {{ scope.row[1] }}
        </template>
      </el-table-column>
</el-table>

</div>  
</template>

<script>
import { searchFree } from "@/api/report";
  export default {
    data() {
      return {
        weeks: [
            {value: 1,label: '第一周'},
            {value: 2,label: '第二周'},
            {value: 3,label: '第三周'},
            {value: 4,label: '第四周'},
            {value: 5,label: '第五周'},
            {value: 6,label: '第六周'},
            {value: 7,label: '第七周'},
            {value: 8,label: '第八周'},
            {value: 9,label: '第九周'},
            {value: 10,label: '第十周'},
            {value: 11,label: '第十一周'},
            {value: 12,label: '第十二周'},
            {value: 13,label: '第十三周'},
            {value: 14,label: '第十四周'},
            {value: 15,label: '第十五周'}, 
            {value: 16,label: '第十六周'},
            {value: 17,label: '第十七周'},
            ],
        days: [
            {value: 1,label: '周一'},
            {value: 2,label: '周二'},
            {value: 3,label: '周三'},
            {value: 4,label: '周四'},
            {value: 5,label: '周五'},
            {value: 6,label: '周六'},
            {value: 7,label: '周日'},
        ],
        lessons:[
            {value: 1,label: '一二节'},
            {value: 2,label: '三四节'},
            {value: 3,label: '五六节'},
            {value: 4,label: '七八节'},
            {value: 5,label: '九十节'},
            {value: 6,label: '晚课'},
        ],
        weekSearch:'',
        daySearch:'',
        lessonSearch:'',
        res : []
      }
    },
    methods:{
        freeSearch(){
            console.log("week:",this.weekSearch);
            console.log("day",this.daySearch);
            console.log("lesson",this.lessonSearch);
            searchFree({
                week : this.weekSearch,
                day : this.daySearch,
                lesson : this.lessonSearch,
            }).then(response => {            
            this.res = response.data
            console.log('response',this.res);
        })
      }
    }
}

</script>
