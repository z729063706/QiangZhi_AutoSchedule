<template>
    <el-table
      v-loading="listLoading"
      :data="labelDetailList"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
    >  
</template>


<script>
import{getStudents} from "@/api/report";
export default {
    data(){
        return{
            stuInfo : [],
            department : '',
        }
    },
    mounted(){
        getStudents({
            department : this.department
        }).then(respose => {
            this.stuInfo = respose.data;
        }
        )
    }
}
</script>>