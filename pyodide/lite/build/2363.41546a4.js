"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[2363,125],{99308:(s,n,e)=>{e.r(n),e.d(n,{ISessions:()=>t,Sessions:()=>r});var i=e(21961);const t=new i.Token("@jupyterlite/session:ISessions");var o=e(76107),d=e(14931);class r{constructor(s){this._sessions=[],this._pendingRestarts=new Set,this._kernels=s.kernels,this._kernels.changed.connect(((s,n)=>{var e,i;switch(n.type){case"remove":{const s=null===(e=n.oldValue)||void 0===e?void 0:e.id;if(!s)return;const i=this._sessions.find((n=>{var e;return(null===(e=n.kernel)||void 0===e?void 0:e.id)===s}));if(!i)return;this._pendingRestarts.add(s),setTimeout((async()=>{this._pendingRestarts.has(s)&&(this._pendingRestarts.delete(s),await this.shutdown(i.id))}),100);break}case"add":{const s=null===(i=n.newValue)||void 0===i?void 0:i.id;if(!s)return;this._pendingRestarts.delete(s);break}}}))}async get(s){const n=this._sessions.find((n=>n.id===s));if(!n)throw Error(`Session ${s} not found`);return n}async list(){return this._sessions}async patch(s){const{id:n,path:e,name:t,kernel:d}=s,r=this._sessions.findIndex((s=>s.id===n)),a=this._sessions[r];if(!a)throw Error(`Session ${n} not found`);const l={...a,path:null!=e?e:a.path,name:null!=t?t:a.name};if(d)if(d.id){const s=this._sessions.find((s=>{var n;return(null===(n=s.kernel)||void 0===n?void 0:n.id)===(null==d?void 0:d.id)}));s&&(l.kernel=s.kernel)}else if(d.name){const s=await this._kernels.startNew({id:i.UUID.uuid4(),name:d.name,location:o.PathExt.dirname(l.path)});s&&(l.kernel=s),this._handleKernelShutdown({kernelId:s.id,sessionId:a.id})}return this._sessions[r]=l,l}async startNew(s){var n,e,t,d;const{path:r,name:a}=s,l=this._sessions.find((s=>s.name===a));if(l)return l;const h=null!==(e=null===(n=s.kernel)||void 0===n?void 0:n.name)&&void 0!==e?e:"",u=null!==(t=s.id)&&void 0!==t?t:i.UUID.uuid4(),c=null!==(d=s.name)&&void 0!==d?d:s.path,_=o.PathExt.dirname(s.name)||o.PathExt.dirname(s.path),k=c.includes(":")?c.split(":")[0]:"",v=_.includes(k)?_:`${k}:${_}`,f=await this._kernels.startNew({id:u,name:h,location:v}),p={id:u,path:r,name:null!=a?a:r,type:"notebook",kernel:{id:f.id,name:f.name}};return this._sessions.push(p),this._handleKernelShutdown({kernelId:u,sessionId:p.id}),p}async shutdown(s){var n;const e=this._sessions.find((n=>n.id===s));if(!e)throw Error(`Session ${s} not found`);const i=null===(n=e.kernel)||void 0===n?void 0:n.id;i&&await this._kernels.shutdown(i),d.ArrayExt.removeFirstOf(this._sessions,e)}async _handleKernelShutdown({kernelId:s,sessionId:n}){}}}}]);
//# sourceMappingURL=2363.41546a4.js.map