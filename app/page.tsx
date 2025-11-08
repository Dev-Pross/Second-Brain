export default function Home() {
  return (
    // <div className="flex flex-col justify-center items-center min-h-screen backdrop-blur bg-black/25 ">
    //   <div className="bg-white/10 rounded-xl m-4">
    //     {/* <label htmlFor="name"></label> */}
    //     <input className="placeholder-gray-150  bg-transparent focus:outline-none  text-white p-4 " type="text" placeholder="Enter you name " />
    //   </div>
    // </div>
    <div className="min-h-screen flex items-center">
      <div className="">
        <label htmlFor="name"> Name</label>
        <input type="text" />
      </div>
    </div>
  );
}
